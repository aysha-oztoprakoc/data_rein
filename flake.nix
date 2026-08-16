{
  description = "Reproducible development shell for the data_rein meta harness";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  nixConfig = {
    extra-substituters = [ "http://localhost:8080" ];
    extra-trusted-public-keys = [ "data_rein-1:hfHPGtlX6tbiJPEW43jVt5xzvmPb4zLg2vyA+1L7oUc=" ];
  };

  outputs = { self, nixpkgs, ... }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
    in
    {
      nixosConfigurations.tell = nixpkgs.lib.nixosSystem {
        system = "x86_64-linux";
        modules = [ ./nixos/tell/configuration.nix ];
      };

      devShells = forAllSystems (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        {
          default = pkgs.mkShell {
            buildInputs = [
              pkgs.python311
              pkgs.python311Packages.pip
              pkgs.python311Packages.virtualenv
              pkgs.nodejs_22
              pkgs.sqlite
              pkgs.uv
              pkgs.ollama
              pkgs.stdenv.cc.cc.lib
              pkgs.zlib
            ];

            shellHook = ''
              export DATA_REIN_HOME="''${DATA_REIN_HOME:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
              if [ ! -d ".venv" ]; then uv venv; fi
              source .venv/bin/activate
              export DATA_REIN_WIKI_DB="$DATA_REIN_HOME/knowledge_base/wiki.db"
              export PYTHONPATH="$DATA_REIN_HOME/src:$DATA_REIN_HOME/odysseus"
              export ODY_NODE_NAME="amdy"
              export OLLAMA_MAX_VRAM="8G"
            '';
          };

          tell = pkgs.mkShell {
            buildInputs = [
              pkgs.python311
              pkgs.nodejs_22
              pkgs.sqlite
              pkgs.uv
              pkgs.ollama
            ];
            
            shellHook = ''
              echo "Entering data_rein Nix environment (TELL State Node)"
              if [ ! -d ".venv" ]; then uv venv; fi
              source .venv/bin/activate
              export DATA_REIN_WIKI_DB="$PWD/knowledge_base/wiki.db"
              export PYTHONPATH="$PWD/src:$PWD/odysseus"
              export ODY_NODE_NAME="tell"
              export OLLAMA_MAX_VRAM="6G"
              
              # Pre-provision the required micro-models for the tell node state machine
              echo "Provisioning TELL node state models..."
              # ollama pull qwen2.5-coder:3b
              # ollama pull smollm2:1.7b
            '';
          };
        }
      );
    };
}
