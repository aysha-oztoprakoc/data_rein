How do you structure your NixOS configs? - NixOS Discourse





































[Skip to last reply](https://discourse.nixos.org/t/how-do-you-structure-your-nixos-configs/65851/20)
[Skip to top](https://discourse.nixos.org/t/how-do-you-structure-your-nixos-configs/65851/1)

[Skip to main content](https://discourse.nixos.org/t/how-do-you-structure-your-nixos-configs/65851#main-container)

[![NixOS Discourse](./How do you structure your NixOS configs_ - NixOS Discourse_files/a5e0d7873e3d34aecf874c577c91a1c06490f436.svg)](https://discourse.nixos.org/)



Sign Up

 Log In

* ​
* ​





# [How do you structure your NixOS configs?](https://discourse.nixos.org/t/how-do-you-structure-your-nixos-configs/65851)

You have selected **0** posts.

[select all](https://discourse.nixos.org/t/how-do-you-structure-your-nixos-configs/65851)






[cancel selecting](https://discourse.nixos.org/t/how-do-you-structure-your-nixos-configs/65851)

6.7k

views



21

likes



19

links



10

users



[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/35386_2.png "Victor Borja")
5](https://discourse.nixos.org/u/vic "vic")

[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/31348_2.png "Alex Antonik")
3](https://discourse.nixos.org/u/AlexAntonik "AlexAntonik")

[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/9471_2.png "Pol Dellaiera")
3](https://discourse.nixos.org/u/drupol "drupol")

[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/6501_2.png "Claes ")
2](https://discourse.nixos.org/u/claes "claes")

[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/13099_2.png "Aaron Honeycutt")
2](https://discourse.nixos.org/u/ahoneybun "ahoneybun")

read 

6
min

[Jun 2025](https://discourse.nixos.org/t/how-do-you-structure-your-nixos-configs/65851/1 "Jump to the first post")

1 / 20

Jun 2025

[Jun 2025](https://discourse.nixos.org/t/how-do-you-structure-your-nixos-configs/65851/20)

## post by AlexAntonik on Jun 20, 2025

[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/31348_2.png)](https://discourse.nixos.org/u/alexantonik)

[AlexAntonik](https://discourse.nixos.org/u/alexantonik)

[Jun 2025](https://discourse.nixos.org/t/how-do-you-structure-your-nixos-configs/65851 "Post date")

Hey everyone! I’ve been on NixOS for a few months now and I’m trying to figure out the best way to organize my config. I want something that’s simple to understand but can grow with my setup.

So far I’ve landed on this structure:

```
├── flake.nix
├── core/                    # System-wide common
│   ├── boot.nix
│   ├── fonts.nix
│   ├── packages.nix
│   └── ...
├── home/                    # Home Manager common
│   ├── hyprland/
│   ├── scripts/
│   ├── firefox.nix
│   ├── nvf.nix
│   └── ...
└── hosts/
    ├── default/
    │   ├── default.nix
    │   ├── users.nix
    │   ├── hardware.nix
    │   └── ...
    └── ...
```

My `flake.nix` is pretty straightforward:

```
{
  outputs = { nixpkgs, ... }@inputs:
  let
    system = "x86_64-linux";
    host = "alex";
    username = "alex";
  in {
    nixosConfigurations = {
      ${host} = nixpkgs.lib.nixosSystem {
        inherit system;
        specialArgs = { inherit inputs username host; };
        modules = [ ./hosts/${host} ];
      };
    };
  };
}
```

Then each host pulls in the core system modules and sets up Home Manager:

```
# hosts/default/default.nix
{
  imports = [
    ./users.nix
    ./drivers.nix  
    ./hardware.nix
    ./host-packages.nix
  ];
}

# hosts/default/users.nix  
{
  imports = [
    ./../../core              # All system modules
    inputs.home-manager.nixosModules.home-manager
  ];
  
  home-manager = {
    useUserPackages = true;
    useGlobalPkgs = true;
    users.${username} = {
      imports = [ ./../../home ];  # All HM configs
      home.stateVersion = "24.11";
    };
  };
  
  users.users.${username} = {
    isNormalUser = true;
    extraGroups = [ "wheel" "networkmanager" /* ... */ ];
  };
}
```

The idea is that `core/` has all the system-level common stuff, `home/` has all common home-mgr configs, and each host just have this plus any host-specific tweaks.

I’m pretty happy with how clean this feels, but I’m still relatively new to NixOS so I’m curious:

* How do you organize your configs?
* Any obvious pitfalls with this approach?
* Is splitting core modules this granularly worth it, or overkill?

Would love to hear how others structure their setups!  
[Full config](https://github.com/AlexAntonik/config) if anyone curious






1 Reply

1


 
​

 
​

6.7k

views



21

likes



19

links



10

users



[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/35386_2.png "Victor Borja")
5](https://discourse.nixos.org/u/vic "vic")

[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/31348_2.png "Alex Antonik")
3](https://discourse.nixos.org/u/AlexAntonik "AlexAntonik")

[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/9471_2.png "Pol Dellaiera")
3](https://discourse.nixos.org/u/drupol "drupol")

[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/6501_2.png "Claes ")
2](https://discourse.nixos.org/u/claes "claes")

[![](./How do you structure your NixOS configs_ - NixOS Discourse_files/13099_2.png "Aaron Honeycutt")
2](https://discourse.nixos.org/u/ahoneybun "ahoneybun")

read 

6
min




## post by ahoneybun on Jun 20, 2025




## post by AlexAntonik on Jun 20, 2025




## post by ahoneybun on Jun 20, 2025




## post by drupol on Jun 20, 2025




## post by vic on Jun 20, 2025




## post by claes on Jun 20, 2025




## post by vic on Jun 20, 2025




## post by AlexAntonik on Jun 20, 2025




## post by vic on Jun 20, 2025




## post by claes on Jun 20, 2025




## post by delliott on Jun 21, 2025




## post by fzakaria on Jun 22, 2025




## post by frozen.frog23 on Jun 22, 2025




## post by vic on Jun 22, 2025




## post by drupol on Jun 22, 2025




## post by vic on Jun 22, 2025




## post by drupol on Jun 23, 2025




## post by kaleocheng on Jun 26, 2025




## post by hugosenari on Jun 27, 2025

Reply

  




### New & Unread Topics

Topic list, column headers with buttons are sortable.

| Topic | Replies | Views | Activity |
| --- | --- | --- | --- |
| [Building android apps and a fdroid repo with nix](https://discourse.nixos.org/t/building-android-apps-and-a-fdroid-repo-with-nix/76478) | [0](https://discourse.nixos.org/t/building-android-apps-and-a-fdroid-repo-with-nix/76478/1) | 129 | [Mar 22](https://discourse.nixos.org/t/building-android-apps-and-a-fdroid-repo-with-nix/76478/1) |
| [Nix Software - Major Update](https://discourse.nixos.org/t/nix-software-major-update/76959) | [2](https://discourse.nixos.org/t/nix-software-major-update/76959/1) | 465 | [14d](https://discourse.nixos.org/t/nix-software-major-update/76959/3) |
| [Nix \*could\* be a great build system](https://discourse.nixos.org/t/nix-could-be-a-great-build-system/69658) | [42](https://discourse.nixos.org/t/nix-could-be-a-great-build-system/69658/1) | 2.7k | [Feb 3](https://discourse.nixos.org/t/nix-could-be-a-great-build-system/69658/43) |
| [Fingerprint Reader Options in Gnome - NixOS 25.11](https://discourse.nixos.org/t/fingerprint-reader-options-in-gnome-nixos-25-11/74118) | [5](https://discourse.nixos.org/t/fingerprint-reader-options-in-gnome-nixos-25-11/74118/1) | 271 | [Jan 23](https://discourse.nixos.org/t/fingerprint-reader-options-in-gnome-nixos-25-11/74118/6) |
| [Então é aqui que os nerds se reúne? ( Brasil )](https://discourse.nixos.org/t/entao-e-aqui-que-os-nerds-se-reune-brasil/78004) | [11](https://discourse.nixos.org/t/entao-e-aqui-que-os-nerds-se-reune-brasil/78004/1) | 213 | [30d](https://discourse.nixos.org/t/entao-e-aqui-que-os-nerds-se-reune-brasil/78004/12) |

### Want to read more? [Browse all categories](https://discourse.nixos.org/categories) or [view latest topics](https://discourse.nixos.org/latest).

[Powered by Discourse](https://discourse.org/powered-by)

Hosted by [Flying Circus](https://flyingcircus.io/).



Invalid date


Invalid date