#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import contextlib
import shelve
import datetime




def main(args):
    '''

    :param sys:
    :return:
    '''

    action = ['jobs', 'status', 'completed', 'partDone']
    # with contextlib.closing(shelve.open('data', 'c')) as data:
    #     tasks = data['tasklist']
    #     time = data['time']
    #     tasknames = tasks.keys()

    tasks = {'Version Control': 0, 'Agile Methodology': 0, 'Programming Logic': 0}
    tasknames = tasks.keys()
    if len(args) == 1 and args[0] == 'taskman.py':
        print('Usage Error. Missing Arguments')
    elif len(args) == 2 and args[0] == 'taskman.py' and args[1] == '-h':
        print('Usage: taskman.py taskname action\n\n'
              'Where taskname is the particular task.\n\n'
              '        Action is the command (status, not completed, complete)')
    elif len(args) == 2 and args[1] in action:
        actions(tasks, args)

    elif len(args) == 3 and args[1] in tasknames and args[2] in action:
        taskevaluator(tasks, args)


def taskevaluator(tasks, args):
    '''
    Function to evaluate the arguments an if valid execute!
    :param args:
    :return:
    '''
    if args[2] == 'completed':
        completed(tasks, args[1])

def actions(tasks, args):
    '''
    function to commit tasks
    :param argument:
    :return:
    '''
    if args[1] == 'jobs':
        print(tasks.keys())

    elif args[1] == 'status':
        statusEvaluator(tasks)

def statusEvaluator(tasks):
    f = open('list.txt', 'r')
    w = f.read()
    f.close()
    print(w)



def completed(tasks, arg):
        tasks[arg] = 1
        f = open('list.txt', 'w')
        f.write(str(tasks))
        f.close
        print(arg + ' Completed Successfully')



if __name__ == "__main__":
   main(sys.argv)