# vigtd
a GTD tool based on CLI and edit items use vim, you can simply regard this as a collection of scripts operating your things lists.

# Installation

```bash
$ git clone https://github.com/Diphia/vigtd.git ~/
```
It is recommended to set a soft link to your binary directory, like:
```bash
$ cd ~/vigtd
$ chmod +x vigtd.py
$ ln -s ~/vigtd/vigtd.py ~/.local/bin/vigtd
```

# Usage

## Workflow

1. use `add` to add some tasks to a raw inbox.
2. you will be autimatically prompted to process the content in raw inbox, and you can make them done immediately or set a DDL and move them to todo list.
3. use `ls` or `show todo` to show the current tasks remained to do.
4. 




# CSV Format
## todo_list.csv
```csv
"task_name","task_ddl","(parent_task)"
```

## done_list.csv
```csv
"task_name","task_ddl","task_finish_time","(parent_task)"
```

## cacalled.csv
```csv
"task_name","task_ddl","called_date","comment","parent_task"
```

## repeat_tasks.csv
```csv
"task_name","task_peroid","parent_task"
```
