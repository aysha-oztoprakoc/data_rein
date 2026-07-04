How do you organize your configuration? - Help - NixOS Discourse





































[Skip to last reply](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306/12)
[Skip to top](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306/1)

[Skip to main content](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306#main-container)

[![NixOS Discourse](./How do you organize your configuration_ - Help - NixOS Discourse_files/a5e0d7873e3d34aecf874c577c91a1c06490f436.svg)](https://discourse.nixos.org/)



Sign Up

 Log In

* ​
* ​





# [How do you organize your configuration?](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306)

[Help](https://discourse.nixos.org/c/learn/9)

You have selected **0** posts.

[select all](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306)






[cancel selecting](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306)

12.2k

views



23

likes



11

links



8

users



[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/2029_2.png "Valentin Gagarin")
2](https://discourse.nixos.org/u/fricklerhandwerk "fricklerhandwerk")

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/1160_2.png "Sondre Nilsen")
2](https://discourse.nixos.org/u/sondr3 "sondr3")

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/219_2.png "Robert Helgesson")
2](https://discourse.nixos.org/u/rycee "rycee")

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/2653_2.png "Jacek Generowicz")
2](https://discourse.nixos.org/u/jacg "jacg")

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/2176_2.png "dalto")](https://discourse.nixos.org/u/dalto "dalto")

read 

4
min

[May 2020](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306/1 "Jump to the first post")

1 / 12

May 2020

[Jan 2021](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306/12)

## post by sondr3 on May 21, 2020

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/1160_2.png)](https://discourse.nixos.org/u/sondr3)

[sondr3](https://discourse.nixos.org/u/sondr3)

[May 2020](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306 "Post date")

I’m sure this is a fairly frequent question, however I haven’t seen any concrete discussion on the *whys* and *hows* of your configuration. This is primarily from my search for a solution that I enjoy using, with a primary focus on a consistent configuration across multiple machines. I can elaborate a bit on my own [configuration](https://github.com/sondr3/dotfiles):

* I initially, like everyone, did everything in a single `configuration.nix` file, installed some packages here, configured some things there. Once I installed NixOS on my desktop machine I needed a way to have separate machine configuration but wanted my “userland” to stay the same.
* At some point I figured out I could create machine specific configurations by having a separate `configuration.nix` files that I symlinked from my `~/.dotfiles` repo into `/etc/nixos/configuration.nix` that imported configuration files/ I had something like `graphical.nix` that configured my Plasma/graphical apps that I’d import but keep machine specific configuration in their own `configuration.nix` files.
* I discovered `home-manager` and integrated it into my configuration as a NixOS module, moving over my dotfiles and merging them into my system configuration. I really enjoyed this, sans finding it annoying that I had to rebuild my system to get new changes for small dotfile changes, so I just symlinked parts of the config that I changed all the time instead of building it with Nix (my Emacs configuration especially).
* I then switched to the `unstable` branch for my machines with `nix-channel`. After having tried out [`niv`](https://github.com/nmattia/niv) for some projects where I needed to pin dependencies and seeing a few people try it out on their configuration I switched to using it for managing my channels and overlays. This works, but due to how I’ve configured things I have to rebuild my system twice for it to update to the latest `unstable` as mandated by `niv`… and I managed to completely break my store by not reading the documentation on what a command did and now I can’t update anymore… which leads me to this.

I’m looking at a way to restructure my configuration and dotfiles, not really sure how yet but I liked where I was conceptually heading, a pinned `nixpkgs` version that’s consistent across my machines. I might also try out using `home-manager` as a regular program and not a NixOS module due to frustrations with having to build the system on minor changes.

Anyone willing to share thoughts, experiences on how they ended up with the configuration they have now, pain points, things they want to improve etc? ![:slightly_smiling_face:](./How do you organize your configuration_ - Help - NixOS Discourse_files/slightly_smiling_face.png ":slightly_smiling_face:")






2 Replies

4


 
​

 
​

* [Where does personal configuration go?](https://discourse.nixos.org/t/where-does-personal-configuration-go/7646/4)
* [NixOS Config Base: A modularized base for NixOS configs](https://discourse.nixos.org/t/nixos-config-base-a-modularized-base-for-nixos-configs/28171/2)
* [Seeking Guidance on Best Practices for NixOS Configuration Management](https://discourse.nixos.org/t/seeking-guidance-on-best-practices-for-nixos-configuration-management/50963)

12.2k

views



23

likes



11

links



8

users



[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/2029_2.png "Valentin Gagarin")
2](https://discourse.nixos.org/u/fricklerhandwerk "fricklerhandwerk")

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/1160_2.png "Sondre Nilsen")
2](https://discourse.nixos.org/u/sondr3 "sondr3")

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/219_2.png "Robert Helgesson")
2](https://discourse.nixos.org/u/rycee "rycee")

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/2653_2.png "Jacek Generowicz")
2](https://discourse.nixos.org/u/jacg "jacg")

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/2176_2.png "dalto")](https://discourse.nixos.org/u/dalto "dalto")

read 

4
min




## post by dalto on May 21, 2020

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/2176_2.png)](https://discourse.nixos.org/u/dalto)

[dalto](https://discourse.nixos.org/u/dalto)

[May 2020](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306/2 "Post date")

Mine is not that complicated. I have a git repo with all my nix configs. I clone it to `/etc/nixos/nix-configs`. Inside `nix-configs` is a nix file for each machine plus a modules directory which has any nix modules that are shared between configurations.

When I build a new machine, I just clone nix-configs and edit the configuration.nix so it does nothing but include the hardware-configuration.nix and nix-configs/machine-name.nix.






1


 
​

 
​




## post by ajs124 on May 21, 2020

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/2501_2.png)](https://discourse.nixos.org/u/ajs124)

[ajs124](https://discourse.nixos.org/u/ajs124)

[May 2020](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306/3 "Post date")

You can get an overview on [this wiki page](https://nixos.wiki/wiki/Configuration_Collection).

A common pattern is separate folders for packages, modules, tests and system configs, for example.






1 Reply

1


 
​

 
​




## post by matklad on May 21, 2020

[![](./How do you organize your configuration_ - Help - NixOS Discourse_files/26467_2.png)](https://discourse.nixos.org/u/matklad)

[matklad](https://discourse.nixos.org/u/matklad)

[May 2020](https://discourse.nixos.org/t/how-do-you-organize-your-configuration/7306/4 "Post date")

![](./How do you organize your configuration_ - Help - NixOS Discourse_files/1160_2.png) sondr3:

> I really enjoyed this, sans finding it annoying that I had to rebuild my system to get new changes for small dotfile changes, so I just symlinked parts of the config that I changed all the time instead of building it with Nix (my Emacs configuration especially).

Yeah, I also struggling with organizing dotfiles. I’ve looked at the home manager, but it seems like it solves a slightly different problem.

What I ended up with is a `home` directory in my config repo, and a [`sync.py`](https://github.com/matklad/config/blob/b2a343330edfdaccdee27980c887e60c8a71dfd0/home/sync.py) script which recursively symlinks stuff, which I run manually. Instead of `sync.py`, I’d love to just say “sync /home/matklad/config/home to /home/matklad” in my `configuration.nix`, but I don’t know how.






2 Replies

1


 
​

 
​




## post by xte on May 21, 2020




## post by sondr3 on May 21, 2020




## post by fricklerhandwerk on May 22, 2020



1 month later

## post by jacg on Jun 22, 2020




## post by fricklerhandwerk on Jun 22, 2020




## post by rycee on Jun 22, 2020




## post by jacg on Jun 23, 2020



7 months later

## post by rycee on Jan 23, 2021

Reply

  




### New & Unread Topics

Topic list, column headers with buttons are sortable.

| Topic | Replies | Views | Activity |
| --- | --- | --- | --- |
| [Build error: llvmPackages.libunwind](https://discourse.nixos.org/t/build-error-llvmpackages-libunwind/66874)  [Help](https://discourse.nixos.org/c/learn/9) | [3](https://discourse.nixos.org/t/build-error-llvmpackages-libunwind/66874/1) | 143 | [Jul 2025](https://discourse.nixos.org/t/build-error-llvmpackages-libunwind/66874/4) |
| [Heroic Launcher native Linux Games have no audio](https://discourse.nixos.org/t/heroic-launcher-native-linux-games-have-no-audio/68615)  [Help](https://discourse.nixos.org/c/learn/9) | [0](https://discourse.nixos.org/t/heroic-launcher-native-linux-games-have-no-audio/68615/1) | 293 | [Aug 2025](https://discourse.nixos.org/t/heroic-launcher-native-linux-games-have-no-audio/68615/1) |
| [How to temporarily “disable” packages (without uninstalling anything)](https://discourse.nixos.org/t/how-to-temporarily-disable-packages-without-uninstalling-anything/67859)  [Help](https://discourse.nixos.org/c/learn/9) | [2](https://discourse.nixos.org/t/how-to-temporarily-disable-packages-without-uninstalling-anything/67859/1) | 195 | [Aug 2025](https://discourse.nixos.org/t/how-to-temporarily-disable-packages-without-uninstalling-anything/67859/3) |
| [How can I create and run this python script in NixOS?](https://discourse.nixos.org/t/how-can-i-create-and-run-this-python-script-in-nixos/71446)  [Help](https://discourse.nixos.org/c/learn/9) | [2](https://discourse.nixos.org/t/how-can-i-create-and-run-this-python-script-in-nixos/71446/1) | 153 | [Oct 2025](https://discourse.nixos.org/t/how-can-i-create-and-run-this-python-script-in-nixos/71446/3) |
| [KDE Connect not working with a specefic machine](https://discourse.nixos.org/t/kde-connect-not-working-with-a-specefic-machine/71790)  [Help](https://discourse.nixos.org/c/learn/9) | [0](https://discourse.nixos.org/t/kde-connect-not-working-with-a-specefic-machine/71790/1) | 74 | [Nov 2025](https://discourse.nixos.org/t/kde-connect-not-working-with-a-specefic-machine/71790/1) |

### Want to read more? Browse other topics in [Help](https://discourse.nixos.org/c/learn/9) or [view latest topics](https://discourse.nixos.org/latest).

[Powered by Discourse](https://discourse.org/powered-by)

Hosted by [Flying Circus](https://flyingcircus.io/).



Invalid date


Invalid date