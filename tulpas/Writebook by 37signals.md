**Writebook by 37signals** is a free, self-hosted web publishing platform designed to let users instantly publish text and images in a clean, browsable online book format. Launched as part of the [ONCE product line](https://once.com/)—which champions a "buy once, own forever" philosophy to counter standard software-as-a-service (SaaS) models—Writebook departs from its sibling applications by being **entirely free to use**. \[[1](https://www.mgmarlow.com/words/2024-10-13-exploring-writebook/), [2](https://books.37signals.com/2/the-writebook-manual), [3](https://books.37signals.com/2/the-writebook-manual/174/welcome)\]

Because it is self-hosted on your own infrastructure, you maintain 100% complete ownership and control over your text, assets, and reader data. \[[1](https://www.mgmarlow.com/words/2024-10-13-exploring-writebook/), [2](https://books.37signals.com/2/the-writebook-manual/174/welcome)\]

Key Features

* **Simple Authoring**: You write and format content using straightforward [Markdown text syntax](https://github.com/basecamp/writebook).  
* **Flexible Page Layouts**: Books can feature customized covers, dedicated title pages, chapters, and picture-focused layouts.  
* **Granular Privacy**: You can seamlessly host a mix of public books for the open web and private books requiring user authentication.  
* **Collaborative Writing**: The software lets you invite co-authors or designated editors to build and refine books together.  
* **Seamless Progress Syncing**: Readers benefit from an intuitive interface that automatically tracks their reading progress across device types.  
* **Open Source Visibility**: 37signals includes the underlying Ruby on Rails source code, letting developers study, tweak, or extend it. \[[1](https://www.mgmarlow.com/words/2024-10-13-exploring-writebook/), [2](https://github.com/basecamp/writebook), [3](https://world.hey.com/jason/introducing-writebook-e217cae3), [4](https://github.com/basecamp/writebook/blob/main/README.md), [5](https://once.com/writebook), [6](https://books.37signals.com/2/the-writebook-manual/30/publishing-on-the-web), [7](https://books.37signals.com/2/the-writebook-manual/26/creating-your-book)\]

Ideal Use Cases

The platform is optimized for clean, long-form presentation rather than traditional blog timelines: \[[1](https://books.37signals.com/2/the-writebook-manual), [2](https://books.37signals.com/2/the-writebook-manual/174/welcome)\]

* Technical runbooks and IT guides  
* Company employee handbooks and onboarding docs  
* Product instruction manuals  
* Creative writing, including short stories, poetry, and full novels  
* Family histories and personal graphic memoirs \[[1](https://books.37signals.com/2/the-writebook-manual), [2](https://books.37signals.com/2/the-writebook-manual/174/welcome), [3](https://37signals.com/podcast/once-again/)\]

Hardware & Technical Requirements

To spin up your own instance, you will need a lightweight environment meeting these core criteria: \[[1](https://books.37signals.com/2/the-writebook-manual), [2](https://once.com/writebook)\]

* **Server Power**: Minimum of 1 CPU and 2GB of RAM.  
* **Domain Setup**: Your own domain name or subdomain pointed cleanly to your server IP without active proxying.  
* **Operating System**: A standard Linux VPS or server (cloud providers like [DigitalOcean](https://books.37signals.com/2/the-writebook-manual/27/installation) or Hetzner work perfectly). \[[1](https://books.37signals.com/2/the-writebook-manual), [2](https://once.com/writebook), [3](https://books.37signals.com/2/the-writebook-manual/27/installation)\]

Deployment Steps

Setting up Writebook is designed to be highly accessible and automated: \[[1](https://books.37signals.com/2/the-writebook-manual/27/installation), [2](https://world.hey.com/jason/introducing-writebook-e217cae3), [3](https://once.com/writebook)\]

1. **Get the Installer Link**: Navigate to the [ONCE Writebook storefront](https://once.com/writebook), process the free "checkout," and receive your customized installation script via email. \[[1](https://www.mgmarlow.com/words/2024-10-13-exploring-writebook/), [2](https://once.com/writebook)\]  
2. **Configure DNS**: Point your chosen domain or subdomain directly to the server's public IP address. \[[1](https://books.37signals.com/2/the-writebook-manual/27/installation)\]  
3. **Execute Command**: Establish an SSH connection to your server terminal, paste the single-line installation string from your email, and execute it. \[[1](https://books.37signals.com/2/the-writebook-manual/27/installation)\]  
4. **Finalize Setup**: The installer uses Docker behind the scenes to bundle dependencies, configure the app server, and automatically provisioning an SSL certificate. The setup completes in roughly 5 minutes. \[[1](https://dev.37signals.com/once-app-server/), [2](https://books.37signals.com/2/the-writebook-manual/27/installation)\]

