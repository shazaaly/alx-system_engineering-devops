# 0x06. Regular Expression (Regex) - DevOps

By: Sylvain Kalache

**Auto Review will be launched at the deadline.**

## Concepts

In this project, we will be focusing on the concept of Regular Expression.

## Background Context

In this project, you will be building regular expressions using Oniguruma, a regular expression library used by Ruby by default. It's essential to note that different regular expression libraries may have different properties.

The following Ruby code should be used, and you only need to replace the `regexp` part with your regular expression:

```ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/regexp/).join
```
## Requirements

General requirements for this project:

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the project folder, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
- All your regex must be built for the Oniguruma library

## Quiz Questions

You've completed the quiz successfully! Keep going!

## Tasks

### Task 0: Simply matching School

Requirements:

The regular expression must match the word "School".
Create a Ruby script that accepts one argument and pass it to a regular expression matching method.

Example:

```
$ ./0-simply_match_school.rb School | cat -e
School$
$ ./0-simply_match_school.rb "Best School" | cat -e
School$
$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

Repo:

GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)

Directory: 0x06-regular_expressions

File: 0-simply_match_school.rb

### Task 1: Repetition Token #0

Requirements:

Find the regular expression that will match the given cases.
Create a Ruby script that accepts one argument and pass it to a regular expression matching method.

Repo:

GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)

Directory: 0x06-regular_expressions

File: 1-repetition_token_0.rb

### Task 2: Repetition Token #1

Requirements:

Find the regular expression that will match the given cases.
Create a Ruby script that accepts one argument and pass it to a regular expression matching method.

Repo:

GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)

Directory: 0x06-regular_expressions

File: 2-repetition_token_1.rb

### Task 3: Repetition Token #2

Requirements:

Find the regular expression that will match the given cases.
Create a Ruby script that accepts one argument and pass it to a regular expression matching method.

Repo:

GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)

Directory: 0x06-regular_expressions

File: 3-repetition_token_2.rb

### Task 4: Repetition Token #3

Requirements:

Find the regular expression that will match the given cases.
Create a Ruby script that accepts one argument and pass it to a regular expression matching method.
Your regex should not contain square brackets.

Repo:

GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)

Directory: 0x06-regular_expressions

File: 4-repetition_token_3.rb

### Task 5: Not quite HBTN yet

Requirements:

The regular expression must exactly match a string that starts with "h", ends with "n", and can have any single character in between.
Create a Ruby script that accepts one argument and pass it to a regular expression matching method.

Example:

```
$ ./5-beginning_and_end.rb 'hn' | cat -e
$
$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
```

Repo:

GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)

Directory: 0x06-regular_expressions

File: 5-beginning_and_end.rb

### Task 6: Call me maybe

Requirement:

The regular expression must match a 10-digit phone number.
Create a Ruby script that accepts one argument and pass it to a regular expression matching method.

Example:

```
$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
$ ./6-phone_number.rb " 4155049898" | cat -e
$
$ ./6-phone_number.rb "415 504 9898" | cat -e
$
$ ./6-phone_number.rb "415-504-9898" | cat -e
$
```

Repo:

GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)

Directory: 0x06-regular_expressions

File: 6-phone_number.rb

### Task 7: OMG WHY ARE YOU SHOUTING?

Requirement:

The regular expression must match only capital letters.
Create a Ruby script that accepts one argument and pass it to a regular expression matching method.

Example:

```
$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
```

Repo:

GitHub repository: [alx-system_engineering-devops](https://github.com/yourusername/alx-system_engineering-devops)

Directory: 0x06-regular_expressions

File: 7-OMG_WHY_ARE_Y