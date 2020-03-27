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




# CSV Format
## todo_list.csv
```csv
"task_name","task_ddl"
```

## done_list.csv
```csv
"task_name","task_ddl","task_finish_time"
```

## cacalled.csv
```csv
"task_name","task_ddl","called_date","comment"
```

## repeat_tasks.csv
```csv
"task_name","task_peroid"
```
