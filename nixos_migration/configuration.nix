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
  # Enable networking
  networking.networkmanager.enable = true;

  # Ensure the specific interface uses DHCP (as requested for 192.168.0.2)
  networking.interfaces.enp0s31f6.useDHCP = true;

  # Set your time zone.
  time.timeZone = "America/Sao_Paulo"; # Adjust if necessary

  # Select internationalisation properties.
  i18n.defaultLocale = "en_US.UTF-8";

  # Enable the OpenSSH daemon.
  services.openssh = {
    enable = true;
    settings.PasswordAuthentication = false;
    settings.PermitRootLogin = "prohibit-password";
  };

  # Users
  users.users.tell = {
    isNormalUser = true;
    description = "Tell AI Node";
    extraGroups = [ "networkmanager" "wheel" "docker" ];
    openssh.authorizedKeys.keys = [
      "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAID8/AhnZmRDO2gyukKsg3GmGuWjc4sdiaU6NYW5GMMI1 workstation-amdy"
    ];
  };

  # Packages for Data Rein and AI
  environment.systemPackages = with pkgs; [
    vim
    git
    curl
    wget
    htop
    # Python + uv
    python3
    uv
    # MQTT
    mosquitto
    # AI Models
    ollama
  ];

  # Docker for heavy workloads if needed
  virtualisation.docker.enable = true;

  # Explicit Mounts for Custom Partitions (to guarantee they are mounted)
  fileSystems."/srv" = {
    device = "/dev/disk/by-uuid/c94a738c-27f3-4929-92fe-20c2fbdb4e48";
    fsType = "ext4";
  };

  fileSystems."/var" = {
    device = "/dev/disk/by-uuid/c8946aa2-e349-4c63-bfc8-ccce9590eaa9";
    fsType = "ext4";
  };
  
  swapDevices = [ { device = "/dev/disk/by-uuid/fe1383a8-be9d-4ecc-b53a-38bf41a09c3e"; } ];

  system.stateVersion = "24.05"; # Did you read the comment?
}
