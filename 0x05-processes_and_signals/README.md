# 0x05. Processes and Signals

## Description

This repository contains the solutions for the "Processes and Signals" project in the DevOps curriculum. The project focuses on understanding processes, signals, and basic process management in Linux. It includes Bash scripts to perform various tasks related to processes and signals.

## Learning Objectives

By the end of this project, learners should be able to explain the following concepts without the help of external resources:

- What is a PID (Process ID)?
- What is a process in Linux?
- How to find a process's PID?
- How to kill a process using signals?
- Understanding signals and their usage.
- Identifying signals that cannot be ignored.

## Resources

The following resources are recommended to read or watch for better understanding of the concepts covered in this project:

- Linux PID
- Linux process
- Linux signal
- Process management in Linux

## Project Structure

The project includes Bash scripts for the following tasks:

1. **What is my PID?** (Script: `0-what-is-my-pid`)
   A script that displays its own PID.

2. **List your processes** (Script: `1-list_your_processes`)
   A script that displays a list of currently running processes, including process hierarchy and other details.

3. **Show your Bash PID** (Script: `2-show_your_bash_pid`)
   A script that displays lines containing the word "bash," allowing the user to easily get the PID of the Bash process.

4. **Show your Bash PID made easy** (Script: `3-show_your_bash_pid_made_easy`)
   A script that displays the PID and process name of processes containing the word "bash."

5. **To infinity and beyond** (Script: `4-to_infinity_and_beyond`)
   A script that displays "To infinity and beyond" indefinitely, with a sleep between each iteration.

6. **Don't stop me now!** (Script: `5-dont_stop_me_now`)
   A script that stops the `4-to_infinity_and_beyond` process using the `kill` command.

7. **Stop me if you can** (Script: `6-stop_me_if_you_can`)
   A script that stops the `4-to_infinity_and_beyond` process without using the `kill` command.

8. **Highlander** (Script: `7-highlander`)
   A script that displays "To infinity and beyond" indefinitely with "I am invincible!!!" upon receiving a SIGTERM signal.

9. **Beheaded process** (Script: `8-beheaded_process`)
   A script that kills the `7-highlander` process.

## Requirements

- Allowed editors: vi, vim, emacs
- All scripts should be interpreted on Ubuntu 20.04 LTS.
- All scripts should end with a new line.
- A `README.md` file, at the root of the project folder, is mandatory.
- All Bash script files must be executable.
- Bash scripts must pass Shellcheck (version 0.7.0 via apt-get) without any error.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining what the script is doing.

## Copyright - Plagiarism

- All solutions for the tasks should be authored independently to meet the learning objectives.
- Publishing the content of this project or any form of plagiarism is strictly forbidden and will result in removal from the ALXSE program.

## Author

- ALXSE
