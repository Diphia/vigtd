#!/usr/bin/python3
# vigtd.py
# diphia@2020
# This script is used to receive the commands and call deeper functions

import sys
#from commands import add,show,raw_process,done
import commands

def command_caller(command_list):
    if(command_list[0] == 'add'):
        commands.add()
        print('Process raw now ? enter y to process, press any other key to skip > ',end = '')
        select = input()
        if(select == 'y'):
            command_caller(['rawpro'])
    elif(command_list[0] == 'rawpro'):
        commands.raw_process()
        print('-----------------------------')
        commands.show('todo')
    elif(command_list[0] == 'show'):
        if(len(command_list) == 1):
            commands.show('todo')
            return None
        commands.show(command_list[1].strip())
    elif(command_list[0] == 'todo'):
        commands.show('todo')
    elif(command_list[0] == 'ls'):
        commands.show('todo')
    elif(command_list[0] == 'done'):
        if(len(command_list) == 1):
            print('Usage: done [id]')
            return None
        print(commands.done(command_list[1].strip()))
        print('-----------------------------')
        commands.show('todo')
    else:
        print('command not found: ' + command_list[0])

def shell():
    while(True):
        try:
            print('vigtd > ',end='')
            input_command = input()
            command_list = input_command.split(' ')
            command_caller(command_list)
        except KeyboardInterrupt:
            exit()

if __name__=="__main__":
    if(len(sys.argv) == 1):
        shell()
    else:
        sys.argv.pop(0)
        command_list = sys.argv
        command_caller(command_list)
