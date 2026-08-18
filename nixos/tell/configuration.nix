# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ config, pkgs, ... }:

{
  imports =
    [ # Include the results of the hardware scan.
      ./hardware-configuration.nix
    ];

  # Bootloader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;

  networking.hostName = "tell"; # Define your hostname.
  networking.networkmanager.enable = true;
  networking.nameservers = [ "1.1.1.1" "8.8.8.8" ];

  # Set your time zone & locale.
  time.timeZone = "America/Sao_Paulo";
  i18n.defaultLocale = "en_US.UTF-8";
  i18n.extraLocaleSettings = {
    LC_ADDRESS = "pt_BR.UTF-8";
    LC_IDENTIFICATION = "pt_BR.UTF-8";
    LC_MEASUREMENT = "pt_BR.UTF-8";
    LC_MONETARY = "pt_BR.UTF-8";
    LC_NAME = "pt_BR.UTF-8";
    LC_NUMERIC = "pt_BR.UTF-8";
    LC_PAPER = "pt_BR.UTF-8";
    LC_TELEPHONE = "pt_BR.UTF-8";
    LC_TIME = "pt_BR.UTF-8";
  };

  # Configure console & X11 keymaps
  services.xserver.xkb = {
    layout = "br";
    variant = "";
  };
  console.keyMap = "br-abnt2";

  # Allow unfree packages (NVIDIA drivers, CUDA, etc.)
  nixpkgs.config.allowUnfree = true;

  # Nix Flakes support
  nix.settings.experimental-features = [ "nix-command" "flakes" ];

  # NVIDIA Proprietary Drivers for Pascal (GTX 1060 requires legacy_580)
  services.xserver.videoDrivers = [ "nvidia" ];
  hardware.graphics.enable = true;
  hardware.nvidia = {
    package = config.boot.kernelPackages.nvidiaPackages.legacy_580;
    modesetting.enable = true;
    open = false; # Proprietary driver is required for Pascal GPUs
    powerManagement.enable = false;
  };

  # Mosquitto MQTT Broker (Core PON Reactive Event Hub)
  services.mosquitto = {
    enable = true;
    listeners = [
      {
        port = 1883;
        address = "0.0.0.0";
        omitPasswordAuth = true;
        acl = [ "topic readwrite #" ];
        settings = {
          allow_anonymous = true;
        };
      }
    ];
  };

  # Ollama Service with CUDA Acceleration
  services.ollama = {
    enable = true;
    package = pkgs.ollama-cuda;
    host = "0.0.0.0";
    port = 11434;
  };

  # Tailscale for secure mesh networking between amdy and tell
  services.tailscale.enable = true;

  # OpenSSH daemon
  services.openssh = {
    enable = true;
    settings = {
      PasswordAuthentication = true;
      PermitRootLogin = "prohibit-password";
    };
  };

  # Open required firewall ports
  networking.firewall = {
    enable = true;
    checkReversePath = "loose";
    allowedTCPPorts = [
      22    # SSH
      1883  # Mosquitto MQTT
      8088  # Sofia FastAPI State Backend
      11434 # Ollama
    ];
  };

  # Sudo without password for automation
  security.sudo.wheelNeedsPassword = false;

  # User account configuration
  users.users."tell" = {
    isNormalUser = true;
    description = "tell";
    extraGroups = [ "networkmanager" "wheel" "video" ];
    openssh.authorizedKeys.keys = [
      "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAID8/AhnZmRDO2gyukKsg3GmGuWjc4sdiaU6NYW5GMMI1 workstation-amdy"
    ];
  };

  # System packages
  environment.systemPackages = with pkgs; [
    git
    vim
    nano
    wget
    curl
    tailscale
    pciutils
    nvtopPackages.nvidia
    htop
    mosquitto
    uv
    python3
    sqlite
  ];

  system.stateVersion = "26.05";
}
