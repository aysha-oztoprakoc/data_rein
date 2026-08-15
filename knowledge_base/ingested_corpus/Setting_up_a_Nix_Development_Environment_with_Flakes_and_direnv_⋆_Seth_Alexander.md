Setting up a Nix Development Environment with Flakes and direnv ⋆ Seth Alexander



[Skip to content](https://sethaalexander.com/setting-up-a-nix-development-environment-with-flakes-and-direnv/#content)


[Seth Alexander](https://sethaalexander.com/)

Father – Dev – Hustler

☰ Menu

* [Home](https://sethaalexander.com/)
* [About Me](https://sethaalexander.com/about-seth-alexander/)

![nix development environment fighting non-declarative options](./Setting up a Nix Development Environment with Flakes and direnv ⋆ Seth Alexander_files/ChatGPT-Image-May-27-2025-10_30_51-PM-1088x725.png)

# Setting up a Nix Development Environment with Flakes and direnv

Posted on [2025-05-282025-05-28](https://sethaalexander.com/setting-up-a-nix-development-environment-with-flakes-and-direnv/) by [Seth Alexander](https://sethaalexander.com/author/sethalexander/)

When I setup my most recent primary development machine I chose [NixOS](https://nixos.org/). I figured, why not. If it doesn’t work out I’ll only be out maybe a day and I’ll have learned I don’t want to do that. However, it ended up working out. With my new found familiarity after a few months using it I decided to take the plunge and spread my Nix chops elsewhere. This meant my MacOS machine. One place I believe Nix can be incredibly powerful is setting up a reproducible Nix development environment. Replacing traditional tools like `nvm`, `pyenv`, and others with a single, powerful solution. I’ll show you how to build a practical setup that automatically activates when you enter your project directory. With this pattern a new developer can onboard installing **TWO**, yes only **TWO**, tools and Nix takes care of the rest.

## What We’ll Build

By the end of this guide, you’ll have a development environment that:

1. **Automatically activates** when you `cd` into your project.
2. **Includes all dependencies** – Python, Node.js, databases, tools.
3. **Is fully reproducible** – works identically on any machine.
4. **Requires zero manual setup** – just clone and start coding.

All defined in a single `flake.nix` file that lives with your code!

## Why Nix? Understanding the Paradigm Shift

Before diving into the setup, let’s understand why Nix represents a fundamental improvement over traditional development environment management tools.

### The Problems with Traditional Tools

Most developers are familiar with version managers like `nvm` (Node Version Manager which shows up in the my post [here](https://sethaalexander.com/freecodecamp-nashville-october-meetup-recap/)), `pyenv` (Python), `rbenv` or `rvm` (Ruby which you may have seen in my post [here](https://sethaalexander.com/fixing-problems-makes-stronger/)), or `rustup` (Rust). While these tools work, they suffer from several fundamental limitations:

1. **Language Silos**: Each language requires its own version manager, leading to a proliferation of tools (`nvm`, `pyenv`, `rbenv`, `jenv`, etc.).
2. **Global State Pollution**: These tools modify global shell state, often conflicting with each other.
3. **Incomplete Isolation**: They only manage language runtimes, not system dependencies, libraries, or tools.
4. **Reproducibility Issues**: “Works on my machine” remains a problem because system-level dependencies aren’t captured.
5. **Manual Synchronization**: Team members must manually ensure they’re using the same versions.

### The Nix Advantage

A Nix development environment solves these problems through a fundamentally different approach:

1. **Declarative Configuration**: Describe what you want, not how to get it.
2. **Complete Isolation**: Each project gets its own isolated environment with all dependencies.
3. **Reproducibility**: The same configuration produces identical environments across machines.
4. **Unified Tool**: Manage any language, tool, or system dependency with one system.
5. **Atomic Operations**: Changes either succeed completely or fail without side effects.
6. **Rollback Capability**: Easily revert to previous configurations.

## Installing Nix with the Determinate Systems Installer

The [Determinate Systems installer](https://github.com/DeterminateSystems/nix-installer) is the recommended way to install Nix. It provides a more reliable and user-friendly installation experience compared to the official installer.

### Installation Steps

1. **Download and run the installer**:

```
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | \
  sh -s -- install
```

2. **Restart your shell** or source the Nix profile:

```
. /nix/var/nix/profiles/default/etc/profile.d/nix-daemon.sh
```

3. **Verify the installation**:

```
nix --version
```

The Determinate Systems installer automatically:

* Enables flakes (experimental feature).
* Sets up the `nix-command` experimental feature.
* Configures better defaults for a smoother experience.
* Provides uninstall capability.

**Note**: All instructions in this guide have been verified to work with Nix 25.05, the latest release.

## Understanding Nix Flakes

Flakes are the modern way to manage Nix projects. They provide:

* **Lock files** for reproducible dependencies.
* **Standard structure** for Nix projects.
* **Composability** between projects.
* **Better evaluation caching**.

### Basic Flake Structure

A flake consists of:

* `flake.nix`: The main configuration file.
* `flake.lock`: Automatically generated lock file (like `package-lock.json`).

## Setting Up direnv for Automatic Environment Loading

[direnv](https://direnv.net/) automatically loads and unloads environment variables and development shells when you enter or leave a directory.

### Installing direnv

Install direnv using your system package manager:

```
# macOS (with Homebrew)
brew install direnv

# Ubuntu/Debian
sudo apt install direnv

# NixOS (add to configuration.nix)
environment.systemPackages = with pkgs; [ direnv ];

# Or using Nix on any system
nix-env -iA nixpkgs.direnv
```

### Shell Integration

Add the following to your shell configuration:

**Bash** (`~/.bashrc`):

```
eval "$(direnv hook bash)"
```

**Zsh** (`~/.zshrc`):

```
eval "$(direnv hook zsh)"
```

**Fish** (`~/.config/fish/config.fish`):

```
direnv hook fish | source
```

### Enhanced Nix Integration

For better Nix flake support, add to `~/.config/direnv/direnvrc`:

```
# Better support for Nix flakes
use_flake() {
  watch_file flake.nix
  watch_file flake.lock
  eval "$(nix print-dev-env)"
}
```

That’s it! direnv is now ready to use with Nix flakes.

## Creating Your First Flake-Based Nix Development Environment

Let’s create a comprehensive example that demonstrates common use cases.

### Project Structure

```
my-project/
├── flake.nix
├── flake.lock
├── .envrc
├── .gitignore
└── src/
```

### The Complete Nix Development Environment Flake Example

Create `flake.nix`:

```
# flake.nix - Nix Flake configuration file
# This file defines a reproducible development environment using Nix flakes
# Documentation: https://nixos.wiki/wiki/Flakes
{
  description = "Development environment with Python and Node.js";

  # Inputs are external dependencies for our flake
  inputs = {
    # nixpkgs is the main package repository for Nix
    # Using "nixos-unstable" gives us the latest packages
    # See available packages at: https://search.nixos.org/packages
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    
    # flake-utils helps us write flakes that work on multiple systems (Linux, macOS)
    # Documentation: https://github.com/numtide/flake-utils
    flake-utils.url = "github:numtide/flake-utils";
  };

  # Outputs define what our flake produces
  outputs = { self, nixpkgs, flake-utils }:
    # This function creates outputs for each system (x86_64-linux, aarch64-darwin, etc.)
    flake-utils.lib.eachDefaultSystem (system:
      let
        # Import nixpkgs for our specific system
        pkgs = nixpkgs.legacyPackages.${system};
        
        # Define Python packages we want
        # The 'ps' parameter is the Python package set
        pythonPackages = ps: with ps; [
          requests    # HTTP library
          pytest      # Testing framework
          black       # Code formatter
        ];
        
        # Create a Python environment with our packages
        pythonEnv = pkgs.python311.withPackages pythonPackages;
        
      in
      {
        # devShells.default is the development environment
        # It's activated with 'nix develop' or automatically via direnv
        # Documentation: https://nixos.wiki/wiki/Development_environment_with_nix-shell
        devShells.default = pkgs.mkShell {
          # Packages to include in the shell environment
          buildInputs = with pkgs; [
            # Python with our selected packages
            pythonEnv
            
            # Node.js (version 24)
            nodejs_24
            
            # Basic development tools
            git         # Version control
            ripgrep     # Fast file search
            jq          # JSON processor
          ];
          
          # Shell hook runs when entering the shell
          # Use this for environment setup, variables, and welcome messages
          shellHook = ''
            echo "🚀 Development environment loaded!"
            echo "📦 Python $(python --version)"
            echo "📦 Node.js $(node --version)"
            echo ""
            echo "Run 'python' or 'node' to start coding!"
          '';
          
          # Environment variables
          # These are set when the shell is active
          PROJECT_NAME = "my-awesome-project";
          NODE_ENV = "development";
        };
      });
}
```

### Setting Up direnv

Create `.envrc`:

```
# This file tells direnv to load our Nix flake environment
# Documentation: https://direnv.net/

# 'use flake' is a direnv command that activates the Nix flake in this directory
# It's equivalent to running 'nix develop' but automatic
use flake

# Optional: Add project-specific environment variables
# These are only set when you're in this directory
REDACTED_BY_SECURITY_SCAN

# Optional: Load secrets from a .env file (don't commit this file!)
# Create a .env file with KEY=value pairs for sensitive data
if [ -f .env ]; then
  dotenv .env
fi
```

### Git Configuration

Create `.gitignore`:

```
# Nix build outputs
result
result-*

# direnv cache
.direnv/

# Environment secrets (never commit these!)
.env
.env.local

# Python
__pycache__/
*.pyc
.pytest_cache/

# Node.js
node_modules/
npm-debug.log*
```

## Using Your Nix Development Environment

1. **Create a new project directory**:

```
mkdir my-project && cd my-project
```

2. **Create the files** shown above:
   * `flake.nix` – Your environment definition
   * `.envrc` – direnv configuration
   * `.gitignore` – Git ignore rules
3. **Allow direnv to load** (you’ll be prompted automatically):

```
direnv allow
```

That’s it! The environment will automatically:

* ✅ Activate when you enter the directory
* ✅ Install all specified packages
* ✅ Set environment variables
* ✅ Deactivate when you leave the directory

Try it out:

```
python --version  # Python 3.11.x
node --version    # v20.x.x
```

## Common Patterns and Next Steps

### Adding More Languages

To add more programming languages to your environment, simply include them in `buildInputs`:

```
buildInputs = with pkgs; [
  pythonEnv
  nodejs_24
  rustc           # Rust compiler
  go              # Go language
  ruby_3_2        # Ruby
  openjdk17       # Java
];
```

### Adding Databases

Need a database for local development?

```
buildInputs = with pkgs; [
  # ... other packages ...
  postgresql_15  # PostgreSQL database
  redis          # Redis key-value store
  sqlite         # SQLite database
];

shellHook = ''
  # ... existing shell hook ...
  
  # Initialize PostgreSQL if needed
  if [ ! -d ".postgres" ]; then
    initdb -D .postgres
    echo "PostgreSQL initialized. Start with: pg_ctl -D .postgres start"
  fi
'';
```

### Finding Packages

To find available packages:

1. Search online: <https://search.nixos.org/packages>
2. Use command line: `nix search nixpkgs package-name`

### Learning More

* **Nix Pills** (beginner tutorial series): <https://nixos.org/guides/nix-pills/>
* **Official Nix Manual**: <https://nixos.org/manual/nix/stable/>
* **Flakes Documentation**: <https://wiki.nixos.org/wiki/Flakes>
* **Nixpkgs Manual**: <https://nixos.org/manual/nixpkgs/stable/>
* **Community Forum**: <https://discourse.nixos.org/>

## Troubleshooting

### “direnv: error .envrc is blocked”

This is a security feature. Run:

```
direnv allow
```

### Flake Changes Not Taking Effect

After modifying `flake.nix`, reload the environment:

```
direnv reload
# or exit and re-enter the directory
```

### Package Not Found

When a package isn’t found, try:

1. Search for the exact name: <https://search.nixos.org/packages>
2. Update your flake: `nix flake update`
3. Some packages have different names in Nix (e.g., `nodejs_2`4 instead of `nodejs`).

## Key Takeaways

1. **One Tool to Rule Them All**: Instead of `nvm`, `pyenv`, etc., use Nix for everything.
2. **Reproducible**: Your teammates get the exact same environment.
3. **Automatic**: With direnv, environments activate automatically.
4. **Declarative**: Describe what you want, not how to install it.
5. **Versioned**: Your environment configuration lives in Git with your code.

Without a doubt the combination of Nix, Flakes, and direnv creates a development experience that’s both powerful and ergonomic, solving the “works on my machine” problem once and for all. I hope this simple guide spurns you to take the plunge and start creating Nix development environments.


Posted in [Tools](https://sethaalexander.com/category/tools/) 

![](./Setting up a Nix Development Environment with Flakes and direnv ⋆ Seth Alexander_files/8c26a2c809f0c39218eb1ec2bf1f51b2f50c971b12e1cdcf9bb8ea4b2a68cad7.png)

## Published by Seth Alexander

[View all posts by Seth Alexander](https://sethaalexander.com/author/sethalexander/)



## Post navigation

[Previous Post Those Who Wander: A Glimpse into America’s Invisible](https://sethaalexander.com/those-who-wander-vivian-ho/)

[Next Post JavaScript Private Elements Trump Compile-Time Illusion](https://sethaalexander.com/javascript-private-elements-trump-compile-time-illusion/)



[Proudly powered by WordPress](http://wordpress.org/)
 | 
Theme: Libre 2 by [Automattic](https://wordpress.com/themes/).