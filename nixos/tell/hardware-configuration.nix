{ config, lib, pkgs, modulesPath, ... }:

{
  imports = [ (modulesPath + "/installer/scan/not-detected.nix") ];

  # NOTE: This file should be replaced by the output of `nixos-generate-config`
  # on the target physical machine. It is provided here as a minimal dummy
  # configuration to allow the flake to evaluate successfully.
  fileSystems."/" = { 
    device = "/dev/disk/by-label/nixos"; 
    fsType = "ext4"; 
  };
  
  boot.initrd.availableKernelModules = [ "nvme" "xhci_pci" "ahci" "usbhid" ];
}
