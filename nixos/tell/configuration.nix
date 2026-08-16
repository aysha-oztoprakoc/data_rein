{ config, pkgs, ... }:

{
  imports = [
    ./hardware-configuration.nix
  ];

  networking.hostName = "tell";

  # Enable Tailscale for internet/SSH overlay network
  services.tailscale.enable = true;
  networking.firewall.checkReversePath = "loose"; # required for Tailscale exit nodes

  # Enable SSH
  services.openssh = {
    enable = true;
    settings = {
      PasswordAuthentication = false;
      PermitRootLogin = "no";
    };
  };

  # Enable Ollama natively on NixOS
  services.ollama = {
    enable = true;
    acceleration = "cuda"; # Specifically for the NVIDIA GTX 1060 on the tell node
    host = "0.0.0.0";
    port = 11434;
  };

  # Open port 11434 for Ollama
  networking.firewall.allowedTCPPorts = [ 11434 ];

  # NVIDIA drivers
  services.xserver.videoDrivers = [ "nvidia" ];
  hardware.graphics.enable = true;
  hardware.nvidia = {
    modesetting.enable = true;
    open = false; # Proprietary drivers usually better for CUDA on Pascal
  };

  users.users.tell = {
    isNormalUser = true;
    extraGroups = [ "wheel" "networkmanager" ];
    openssh.authorizedKeys.keys = [
      # User must add their amdy node's public key here
      "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI_USER_PUBLIC_KEY_HERE amdy@local"
    ];
  };

  environment.systemPackages = with pkgs; [
    git
    vim
    tailscale
    pciutils
    nvtopPackages.nvidia
  ];

  system.stateVersion = "24.05";
}
