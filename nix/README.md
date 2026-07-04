# Nix transition — backup/omarchy → reproducible flake

This directory stages the future migration of the omarchy workstation + data_rein
harness from the current **imperative** backup/restore model to a **declarative**
Nix flake (+ home-manager). Nothing here changes today's behaviour; it exists so the
switch is a refactor, not a rewrite.

## The single manifest

`config/backup_config.json` is already the machine-readable source of truth the
backup system uses. It maps 1:1 onto Nix concepts, so a future flake reads the same
file instead of duplicating the list:

| backup_config.json                | Nix / home-manager target                          |
|-----------------------------------|----------------------------------------------------|
| `dotfiles.paths[]`                | `home-manager` `home.file` / `xdg.configFile` links |
| `health.essential_packages[]`     | `environment.systemPackages` (or `home.packages`)  |
| `health.hypr_critical_files[]`    | assertions in the flake check / `hyprland` module   |
| `harness.repo` + `harness.branch` | a `flake input` (`inputs.data_rein`)               |
| `harness.essential_paths[]`       | files the harness derivation must expose            |
| `remote_restore.github`           | `inputs.data_rein.url` fallback                     |

## Migration path (no big-bang)

1. **Now (imperative):** `reins backup` health-gates shutdowns, keeps a portable
   rescue script, and pushes dotfiles. The rescue script is the offline bridge.
2. **Next (hybrid):** add `nix/flake.nix` that imports `backup_config.json` (via
   `builtins.fromJSON`) to derive `home.packages` and the config symlinks. The
   emergency rescue script keeps working as the live-USB fallback.
3. **Later (declarative):** the workstation is `nixos-rebuild switch`-able; the
   health suite (`reins.services.backup.BackupService.health_check`) becomes a
   `nix flake check`, and "restore" becomes "boot the pinned generation."

## Why the rescue script still matters under Nix

A Nix generation recovers a *configured* system, but not un-tracked state (the wiki
DB, secrets vault, in-flight work). The emergency script (`reins backup emergency`)
and the failsafe snapshots remain the belt-and-suspenders that guarantee the
workspace is never lost — Nix handles reproducibility, the script handles the data.

## TODO for the flake author
- [ ] `nix/flake.nix` reading `../config/backup_config.json`.
- [ ] home-manager module linking `dotfiles.paths` (read-only, so the health checks
      still pass).
- [ ] wire `health.essential_packages` → `home.packages`.
- [ ] a `nix flake check` app that shells `reins backup check`.
