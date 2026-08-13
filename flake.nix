{
  description = "Reproducible development shell for the data_rein meta harness";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { nixpkgs, ... }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
    in
    {
      devShells = forAllSystems (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              git
              pkg-config
              python311
              ruff
              uv
            ];

            buildInputs = with pkgs; [
              libffi
              openssl
              sqlite
              zlib
            ];

            UV_PYTHON_DOWNLOADS = "never";

            shellHook = ''
              export DATA_REIN_HOME="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
            '';
          };
        }
      );
    };
}
