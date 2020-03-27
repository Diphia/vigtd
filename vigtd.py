#!/usr/bin/python3
# vigtd.py
# diphia@2020
# This script is used to receive the commands and call deeper functions

import sys
import os
import commands

from utilities import call_vim_single_line

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
    elif(command_list[0] == 'repeatgen'):
        commands.repeatgen()
    elif(command_list[0] == 'clear'):
        os.system('clear')
    elif(command_list[0] == 'pp' or command_list[0] == 'postpone'):
        if(len(command_list) == 3):
            print(commands.postpone(command_list[1].strip(),command_list[2].strip()))
        else:
            content = call_vim_single_line('Enter target date')
            print(commands.postpone(command_list[1].strip(),content))
        commands.show('todo')
    elif(command_list[0] == 'cancel'):
        print(commands.cancel(command_list[1].strip()))
        commands.show('todo')
    elif(command_list[0] == 'editrep' or command_list[0] == 'editrepeat' or command_list[0] == 'editrp'):
        commands.repeat_edit()
        commands.repeatgen()
    else:
        print('command not found: ' + command_list[0])
        commands.show('todo')

def shell():
    commands.repeatgen()
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
        sys.argv.pop(0) # pop program name 
        command_list = sys.argv
        command_caller(command_list)
