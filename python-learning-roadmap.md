# TaskForge — Learn Python by Building a Project Manager

A project-based Python course built around **one app that grows with you**: a command-line project-management tool called **TaskForge**. You'll start with nothing but the terminal and a list in memory, then add real features one milestone at a time — CRUD, login, permissions, saving to disk, tests, and finally a real interface.

The point is **not** the finished app. The point is that by building it, you'll bump into every important Python concept *because you need it*, not because a tutorial told you to. That's the kind of learning that sticks.

---

## How to use this roadmap

- **Weeks are a guide, not a deadline.** Go faster or slower. Some weeks are heavier than others.
- **Don't skip milestones.** Each one is built on the one before it. If you jump ahead, things won't make sense.
- **Tick the boxes.** Every task is a checkbox `- [ ]`. On GitHub these become clickable tick-boxes — open this file in your repo and check things off as you go.
- **The italic links are your lifeline.** Next to most tasks you'll see *Stuck? → [topic]*. Those go straight to a clear explanation. Read the concept, *then* come back and write the code yourself. Don't copy-paste whole solutions — you'll learn nothing.
- **Do the Git Ritual for every feature.** It's the second section below. This is a habit, not a one-time setup. Pushing your work and using branches is part of *every* milestone, not just Week 1.
- **Finish each milestone properly.** Each one ends with a **Definition of Done** — a short checklist that tells you when you've *actually* finished, not just "it kind of runs."
- **If a link ever shows a 404,** the page probably just moved. Search the site (for example, type `realpython dictionaries` into Google) and you'll find it in seconds.

---

## The Golden Rules

1. **One feature = one branch = one merge.** After Week 1, never write code directly on `main`.
2. **Push at least once every time you sit down to work.** If your laptop dies, your work should already be safe on GitHub.
3. **Commit small and often.** A commit should be one small, complete thought ("add task deletion"), not a whole day of changes dumped at once.
4. **Make it work, *then* make it clean.** Get the feature working first. Then go back and tidy the names, split big functions, remove repetition.
5. **When stuck for more than ~20 minutes, use the "Getting Unstuck" steps** at the bottom of this file — in order. Struggling a little is normal and good. Struggling alone for hours is not.
6. **Read your own error messages.** Python tells you exactly what line broke and why. The answer is usually right there. *Stuck? → [Understanding Python tracebacks](https://realpython.com/python-traceback/)*

---

## The Git Ritual (do this for every single feature)

You'll repeat this loop dozens of times. After a week it'll be muscle memory.

**1. Start a fresh branch from an up-to-date `main`:**
```bash
git checkout main
git pull
git checkout -b feature/add-task     # name it after what you're building
```

**2. While you work — code a little, run it, commit a little:**
```bash
# ...write some code, run your program, check it works...
git add .
git commit -m "Add command to create a new task"
# ...keep going, commit each small working step...
```

**3. When the feature works, push it and merge it in:**
```bash
git push -u origin feature/add-task
```
Then go to your repo on GitHub, open a **Pull Request** (PR) from your branch into `main`, scroll through the "Files changed" tab to **review your own diff** (this catches so many silly mistakes), and click **Merge**.

**4. Clean up and go again:**
```bash
git checkout main
git pull
git branch -d feature/add-task       # delete the finished branch
```

> **Why bother with branches for a solo project?** Because this is exactly how every real software team works, and the habit is worth more than the app. Branches also mean you can experiment freely — if a branch becomes a mess, you just delete it and `main` is untouched.

*Stuck on git itself? → [Learn Git Branching (interactive, do this!)](https://learngitbranching.js.org/) · [Pro Git book](https://git-scm.com/book/en/v2) · [Git & GitHub for beginners](https://docs.github.com/en/get-started/using-git/about-git)*

---

# Milestone 0 — Foundations & Git Setup
### *Week 1 — your first checkpoint, before any TaskForge code*

This whole week is about setting up your tools and your repo *properly* so every later milestone is smooth. No app features yet — just the launchpad.

**What you'll learn:** the command line, installing Python, virtual environments, and the core Git/GitHub workflow.

### Setup checklist
- [ ] Install Python (3.12 or newer). *Stuck? → [Installing Python](https://realpython.com/installing-python/) · [python.org/downloads](https://www.python.org/downloads/)*
- [ ] Confirm it works: open a terminal and run `python --version` (or `python3 --version`).
- [ ] Install a code editor — **VS Code** is the standard. *Stuck? → [Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)*
- [ ] Get comfortable with basic terminal commands: `cd`, `ls`/`dir`, `mkdir`, `pwd`. *Stuck? → [The terminal for beginners](https://www.freecodecamp.org/news/command-line-for-beginners/)*
- [ ] Create a folder `taskforge`, open it in VS Code, and create a file `main.py` that just prints `Hello, TaskForge`. Run it.

### Git & GitHub checklist
- [ ] Install Git. *Stuck? → [git-scm.com/downloads](https://git-scm.com/downloads)*
- [ ] Create a free [GitHub account](https://github.com/signup).
- [ ] Tell Git who you are:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```
- [ ] Walk through GitHub's beginner guide once, end to end. *Stuck? → [GitHub "Hello World" guide](https://docs.github.com/en/get-started/start-your-journey/hello-world)*
- [ ] Create a new **repository** on GitHub called `taskforge` (add a README when prompted).
- [ ] **Clone** it to your computer: `git clone <your-repo-url>` and move your `main.py` into it.
- [ ] Add a **`.gitignore`** file for Python so junk files don't get committed. *Stuck? → [GitHub's Python .gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)*
- [ ] Write a short **`README.md`**: what TaskForge is, and "a project to learn Python." You'll grow this as you go. *Stuck? → [How to write a README](https://www.makeareadme.com/)*
- [ ] Make your first real commit and push it:
  ```bash
  git add .
  git commit -m "Initial project setup"
  git push
  ```

### Practice the branch workflow (this is the important bit)
- [ ] Create a branch `feature/welcome-message`. *Stuck? → [Learn Git Branching](https://learngitbranching.js.org/)*
- [ ] On that branch, change your program to print a nicer welcome banner.
- [ ] Commit, push the branch, open a Pull Request on GitHub, review the diff, and merge it into `main`.
- [ ] Switch back to `main`, pull, and delete the branch. **You just did the full Git Ritual — you'll repeat this all course long.**

### Bonus
- [ ] Create and activate a **virtual environment** (`python -m venv .venv`) and learn what it's for. *Stuck? → [Virtual environments primer](https://realpython.com/python-virtual-environments-a-primer/)*

> **Definition of Done:** Your `taskforge` repo is on GitHub, you've made commits on `main` *and* successfully merged at least one feature branch via a PR, and you can explain (out loud, to yourself) what `add`, `commit`, `push`, `branch`, and `merge` each do.

---

# Milestone 1 — A Working CRUD App (in memory, command line only)
### *Weeks 2–4 — the heart of the course*

No files, no database, no UI. Everything lives in a Python list while the program runs (and disappears when it closes — that's fine for now). This is where you'll learn the real fundamentals of programming.

**Core idea:** A **task** is a small bundle of information. You'll store tasks in a list and write code to **C**reate, **R**ead, **U**pdate, and **D**elete them — the four things every app does.

> **Git reminder:** branch for each piece — `feature/add-task`, `feature/list-tasks`, `feature/menu-loop`, etc. Push and merge each one.

## Week 2 — Create & Read

**What you'll learn:** variables, dictionaries, lists, `print()`, `input()`, f-strings, and the main loop that keeps a program running.

- [ ] Represent a single task as a **dictionary**, e.g. `{"id": 1, "title": "Buy milk", "status": "todo"}`. Start minimal — just these three fields. *Stuck? → [Dictionaries](https://realpython.com/python-dicts/)*
- [ ] Store all tasks in a **list**. *Stuck? → [Lists and tuples](https://realpython.com/python-lists-tuples/)*
- [ ] Build an **"add task"** action: ask the user for a title with `input()`, build the dictionary, and append it to the list. *Stuck? → [Reading input with input()](https://realpython.com/python-input-output/) · [f-strings for nice text](https://realpython.com/python-f-strings/)*
- [ ] Build a **"list all tasks"** action that loops through the list and prints each task neatly (e.g. `[1] Buy milk — todo`). *Stuck? → [for loops](https://realpython.com/python-for-loop/)*
- [ ] Build a **menu loop**: show options (1 = add, 2 = list, 3 = quit) on repeat until the user chooses quit. *Stuck? → [while loops](https://realpython.com/python-while-loop/) · [if/elif/else](https://realpython.com/python-conditional-statements/)*
- [ ] Auto-assign each new task a unique `id` (a counter that goes up each time).

**Stretch:** add more fields to a task — a `priority` ("low"/"medium"/"high") and a `description`.

> **Definition of Done:** You can run the program, add several tasks, list them, and quit cleanly — all from the menu.

## Week 3 — Update & Delete

**What you'll learn:** finding items in a list, modifying data, removing data, and writing your first reusable functions.

- [ ] Build a **"find task by id"** helper that searches the list and returns the matching task (or tells the user it doesn't exist). *Stuck? → [Looping techniques](https://realpython.com/python-for-loop/)*
- [ ] Build an **"update task"** action: pick a task by id, then change its title or status. *Stuck? → [Modifying dictionaries](https://realpython.com/python-dicts/)*
- [ ] Build a **"mark as done"** shortcut that sets a task's status to `"done"`.
- [ ] Build a **"delete task"** action that removes a task by id from the list. *Stuck? → [Removing list items](https://realpython.com/python-lists-tuples/)*
- [ ] You now have full **CRUD**! Add these to your menu.
- [ ] Start moving repeated code into **functions** — e.g. `add_task()`, `list_tasks()`, `delete_task()`. Each function should do one job. *Stuck? → [Defining your own functions](https://realpython.com/defining-your-own-python-function/)*

**Stretch:** add a "filter" view — show only tasks with a given status (just the `todo`s, or just the `done`s).

> **Definition of Done:** All four CRUD operations work from the menu, and your code is organized into named functions instead of one giant block.

## Week 4 — Validation & not crashing

**What you'll learn:** input validation and handling errors gracefully so a wrong keypress doesn't kill the whole program.

- [ ] Handle the user typing something silly — letters where you expected a number, or an id that doesn't exist — *without crashing*. *Stuck? → [Exceptions & try/except](https://realpython.com/python-exceptions/)*
- [ ] Don't allow empty task titles.
- [ ] Restrict `status` to a fixed set of allowed values; reject anything else.
- [ ] Show friendly messages: "No task with id 7", "Please enter a number", etc.
- [ ] Refactor: read back through your whole program and improve variable/function names so they say what they mean. *Stuck? → [Writing clean Python (PEP 8)](https://realpython.com/python-pep8/)*

**Stretch:** add a simple **search** — type part of a title and list all matching tasks.

> **Definition of Done:** You can mash random/wrong inputs into every menu option and the program never crashes — it just tells you politely what went wrong.

---

# Milestone 2 — Structure It Like Real Software
### *Week 5 — from "a script" to "a program"*

Your `main.py` is probably getting long. Time to learn how real Python projects are organized, and to model your data with **classes** instead of loose dictionaries.

**What you'll learn:** classes and objects, modules/files, enums, type hints, and dataclasses.

- [ ] Turn a task into a **class** with attributes (`id`, `title`, `status`, `priority`) and methods (e.g. `mark_done()`). *Stuck? → [Object-oriented programming in Python](https://realpython.com/python3-object-oriented-programming/)*
- [ ] Create a `TaskManager` class that holds the list of tasks and has the methods `add`, `get`, `update`, `delete`, `all`. This is the "brain" of your app. *Stuck? → [OOP in Python](https://realpython.com/python3-object-oriented-programming/)*
- [ ] Use an **Enum** for status and priority instead of bare strings — it prevents typos like `"dnoe"`. *Stuck? → [Enums in Python](https://realpython.com/python-enum/)*
- [ ] Split your code into **separate files/modules**: e.g. `models.py` (the classes), `manager.py` (the TaskManager), `cli.py` (the menu/printing), and a thin `main.py` that just starts things. *Stuck? → [Modules and packages](https://realpython.com/python-modules-packages/)*
- [ ] Add **type hints** to your functions and methods so it's clear what goes in and comes out. *Stuck? → [Type checking & hints](https://realpython.com/python-type-checking/)*

**Stretch:** rewrite your Task class as a **dataclass** to cut boilerplate. *Stuck? → [Data classes](https://realpython.com/python-data-classes/)*

> **Definition of Done:** No single file is doing everything. Tasks are real objects with methods, status/priority are Enums, and you could explain why splitting the code into modules makes it easier to work with.

---

# Milestone 3 — Users: Authentication & Authorization
### *Weeks 6–7 — who are you, and what are you allowed to do?*

Now TaskForge gets multi-user. **Authentication** = proving who you are (login). **Authorization** = what you're allowed to do once you're in (permissions). This is a great place to learn about security basics.

> **Git reminder:** `feature/user-model`, `feature/login`, `feature/password-hashing`, `feature/roles`…

## Week 6 — Authentication (registration & login)

**What you'll learn:** modeling users, the critical rule of *never storing plain-text passwords*, and hashing.

- [ ] Create a **`User`** class (`username`, `password_hash`, `role`). *Stuck? → [OOP in Python](https://realpython.com/python3-object-oriented-programming/)*
- [ ] Build **register**: create a new user, refusing duplicate usernames.
- [ ] **Never store the raw password.** Store a **hash** of it. Learn what hashing is and why it matters. *Stuck? → [Hashing passwords with bcrypt](https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/) · [Python `hashlib`](https://docs.python.org/3/library/hashlib.html)*
- [ ] Build **login**: hash the entered password and compare it to the stored hash. Match = logged in.
- [ ] Track the **current logged-in user** (a "session") so the rest of the app knows who's acting.
- [ ] Hide the password as it's typed using `getpass`. *Stuck? → [`getpass` docs](https://docs.python.org/3/library/getpass.html)*

**Why hashing matters (read this):** A hash is a one-way scramble — you can't turn it back into the password. So even if someone steals your data, they don't get the actual passwords. *Stuck? → [Hashing passwords with bcrypt](https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/)*

> **Definition of Done:** You can register users and log in/out. Nowhere in your program is a real password stored as plain text — only hashes.

## Week 7 — Authorization (roles, ownership & permissions)

**What you'll learn:** roles, ownership of data, and protecting actions behind permission checks.

- [ ] Give users a **role**: `admin` or `member`.
- [ ] Make tasks (and projects, below) belong to a user — store the **owner**.
- [ ] Enforce rules: a member can only edit/delete **their own** tasks; an admin can do anything.
- [ ] Block actions for users who aren't logged in.
- [ ] Learn **decorators** and use one to wrap actions that require login or admin rights (e.g. `@requires_login`). This is a clean, professional way to do permission checks. *Stuck? → [Primer on decorators](https://realpython.com/primer-on-python-decorators/)*

**Introduce a second entity — Projects (great CRUD + authz practice):**
- [ ] Add a **`Project`** class (`id`, `name`, `owner`). A project groups tasks together.
- [ ] Give each task a `project_id` so tasks live inside projects.
- [ ] Add CRUD for projects, with the same ownership rules.

**Stretch:** add the idea of **assigning** a task to another user (an "assignee" separate from the owner).

> **Definition of Done:** Logging in as different users genuinely changes what you can see and do. A member cannot delete someone else's task; an admin can. Permission checks are enforced in code, not just on the honor system.

---

# Milestone 4 — Make It Remember: Saving to Disk
### *Weeks 8–9 — persistence with files, then a database*

Right now everything vanishes when you quit. Let's fix that. You'll learn file input/output, then graduate to a real (tiny) database.

> **Git reminder:** `feature/save-load-json`, `feature/autosave`, `feature/sqlite`…

## Week 8 — Save & load with JSON

**What you'll learn:** reading and writing files, the `with` statement, JSON, and file paths.

- [ ] Learn how to **read from and write to a file**. *Stuck? → [Reading and writing files](https://realpython.com/read-write-files-python/) · [The `with` statement](https://realpython.com/python-with-statement/)*
- [ ] Learn **JSON** — the standard text format for saving structured data. *Stuck? → [Working with JSON in Python](https://realpython.com/python-json/)*
- [ ] **Save** all tasks, projects, and users to a `.json` file when the program exits (or after each change).
- [ ] **Load** that file when the program starts, so your data is still there. Handle the "file doesn't exist yet" case gracefully.
- [ ] Use **`pathlib`** to handle file paths properly instead of hardcoding them. *Stuck? → [`pathlib` guide](https://realpython.com/python-pathlib/)*

**Watch out:** your `User` objects, Enums, etc. need to be converted to/from plain dictionaries to fit in JSON. Figuring out that conversion *is* the lesson.

**Stretch:** add an **export to CSV** feature so tasks can open in a spreadsheet. *Stuck? → [Reading & writing CSV](https://realpython.com/python-csv/)*

> **Definition of Done:** You can add tasks, quit the program completely, reopen it, and your tasks are still there.

## Week 9 — Upgrade to a real database (SQLite)

**What you'll learn:** databases and a first taste of SQL — and why a database beats a giant JSON file once data grows. SQLite is built into Python; no install needed.

- [ ] Learn the basics of **SQLite** and SQL (`CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`). *Stuck? → [`sqlite3` docs](https://docs.python.org/3/library/sqlite3.html) · [Python SQL libraries](https://realpython.com/python-sql-libraries/)*
- [ ] Create tables for `users`, `projects`, and `tasks`.
- [ ] Rewrite your manager classes to read/write from the database instead of the JSON file.
- [ ] Notice how the CRUD methods you already built map almost one-to-one onto SQL commands.

**Stretch:** learn how the three tables **relate** (a task belongs to a project; a project belongs to a user) and how to query across them.

> **Definition of Done:** TaskForge stores everything in a real SQLite database file, and all your CRUD still works through it.

---

# Milestone 5 — Make It Trustworthy: Testing & Polish
### *Week 10 — prove it works, and keep it that way*

Real software has tests so you can change things without secretly breaking something else. This is a habit that makes you dramatically more confident as a programmer.

**What you'll learn:** automated testing, logging, and documenting code.

- [ ] Learn how testing works in Python and write your first tests. *Stuck? → [Getting started with testing](https://realpython.com/python-testing/)*
- [ ] Use **pytest** to write tests for your manager: adding a task, deleting a task, blocking a permission, etc. *Stuck? → [Effective testing with pytest](https://realpython.com/pytest-python-testing/)*
- [ ] Add a test that proves a member *can't* delete another user's task.
- [ ] Add **logging** so the program can record what happened (instead of random `print`s). *Stuck? → [Logging in Python](https://realpython.com/python-logging/)*
- [ ] Write **docstrings** for your classes and functions. *Stuck? → [Documenting Python code](https://realpython.com/documenting-python-code/)*
- [ ] Update your **README** with how to run the app and run the tests.

**Stretch:** set up a **GitHub Action** that runs your tests automatically every time you push. (This is "CI" — continuous integration — and it's how real teams catch bugs.) *Stuck? → [GitHub Actions for Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)*

> **Definition of Done:** You can run `pytest` and watch a suite of tests pass. If you break something on purpose, a test goes red and tells you.

---

# Milestone 6 — Give It a Face: User Interfaces
### *Weeks 11–12+ — the payoff*

Everything so far runs through a text menu. Now you'll put a real interface on top of the exact same "brain" (your manager classes). The big lesson here: **a good UI is just a new front door onto logic you already built.** You shouldn't have to rewrite TaskForge's core — only how the user interacts with it.

Pick **one** path to start (then try another for fun):

## Path A — Terminal UI with Textual *(recommended next step)*
A modern, good-looking app that still runs in the terminal — buttons, lists, inputs, the works. It's the most natural jump from a command-line app.
- [ ] Work through the official tutorial (you'll build a stopwatch). *Stuck? → [Textual tutorial](https://textual.textualize.io/tutorial/)*
- [ ] Learn the framework's pieces — widgets, layout, and events. *Stuck? → [Build beautiful terminal UIs with Textual](https://realpython.com/python-textual/)*
- [ ] Build a TaskForge screen: a list of tasks, plus buttons/inputs to add, complete, and delete them — all calling your existing manager methods.
- [ ] Bonus: a full worked example combining a TUI with a database. *Reference → [Build a Contact Book with Textual & SQLite](https://realpython.com/contact-book-python-textual/)*

## Path B — Desktop GUI with Tkinter
A classic windowed app with buttons and text boxes. Tkinter ships with Python.
- [ ] Learn Tkinter basics — windows, labels, buttons, entry fields. *Stuck? → [Python GUI programming with Tkinter](https://realpython.com/python-gui-tkinter/)*
- [ ] Build a window that lists tasks and lets you add/complete/delete them via your manager.

## Path C — Web app with Flask
Put TaskForge in the browser. This opens the door to web development.
- [ ] Learn Flask basics — routes, templates, forms. *Stuck? → [Flask official quickstart](https://flask.palletsprojects.com/en/stable/quickstart/) · [Flask by example](https://realpython.com/flask-by-example-part-1-project-setup/)*
- [ ] Build pages to view tasks and a form to add them, wired to your manager.

> **Definition of Done:** TaskForge has a real interface where you can do the core actions (add, view, complete, delete) by clicking/typing in a UI — and the underlying logic is the same code you built in the earlier milestones.

---

## You finished. Now what?

If you've made it here, you've touched nearly every fundamental in Python *and* learned how real software is built and shipped. Some directions to keep growing:

- [ ] **Add due dates and reminders** — learn the `datetime` module. *Stuck? → [Python `datetime` guide](https://realpython.com/python-datetime/)*
- [ ] **Turn it into a real web API** with FastAPI or Flask so a phone app could talk to it. *Stuck? → [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)*
- [ ] **Package it** so others can install it with `pip`. *Stuck? → [Publishing a package](https://realpython.com/pypi-publish-python-package/)*
- [ ] **Write a proper project README** with screenshots, and pin the repo on your GitHub profile — it's a genuine portfolio piece now.
- [ ] **Start a brand-new project** and do it all again without the training wheels. That's when it really clicks.

---

## Getting Unstuck (follow these in order)

When you've been stuck for ~20 minutes, work down this list — don't skip to the bottom:

1. **Read the error message carefully.** It names the file, the line, and the problem. *→ [Reading tracebacks](https://realpython.com/python-traceback/)*
2. **Re-read the task and the linked concept page.** The answer is usually in there.
3. **Print things out.** Add `print()` lines to see what your variables actually contain right before it breaks. (This is real debugging — pros do it constantly.)
4. **Rubber-duck it.** Explain the problem out loud, line by line, to a literal object or to me. Half the time you'll spot the bug mid-sentence.
5. **Search the exact error message** (copy-paste it). Someone has hit it before.
6. **Make the smallest possible version** that reproduces the problem, then fix that.
7. **Then ask a human (or me).** When you ask, say: what you're trying to do, what you expected, what actually happened (paste the error), and what you've already tried. Asking a good question is itself a skill worth practicing.

---

## Mini-glossary

- **CRUD** — Create, Read, Update, Delete: the four basic things apps do to data.
- **CLI** — Command-Line Interface: interacting with a program by typing text.
- **Authentication** — proving *who you are* (logging in).
- **Authorization** — what you're *allowed to do* once logged in (permissions).
- **Hashing** — a one-way scramble of data (like a password) that can't be reversed.
- **Persistence** — making data survive after the program closes (saving to disk).
- **Repository (repo)** — the folder of your project that Git tracks.
- **Branch** — a separate line of work in Git, so you can build a feature without touching `main`.
- **Commit** — a saved snapshot of your changes with a message describing them.
- **Pull Request (PR)** — a request to merge one branch into another, where you review the changes first.
- **Refactor** — improving the structure of working code without changing what it does.

---

## The whole journey at a glance

- **Milestone 0 (Wk 1):** Tools + Git/GitHub set up. → *first checkpoint*
- **Milestone 1 (Wk 2–4):** CRUD in memory, command line.
- **Milestone 2 (Wk 5):** Classes, modules, clean structure.
- **Milestone 3 (Wk 6–7):** Login (authentication) + permissions (authorization).
- **Milestone 4 (Wk 8–9):** Save to files (JSON) → then a database (SQLite).
- **Milestone 5 (Wk 10):** Tests, logging, docs.
- **Milestone 6 (Wk 11–12+):** A real UI (terminal, desktop, or web).

**Remember the Golden Rules. Branch, commit, push — every feature, every time. Have fun building.**
