import sys
import contextlib
import datetime




def main(args):
    '''

    :param sys:
    :return:
    '''

    action = ['jobs', 'status', 'completed', 'partDone']
    # try:
    #     with contextlib.closing(shelve.open(data, 'c')) as data:
    #         tasks = data['tasklist']
    #         time = data['time']
    #         tasknames = tasks.keys()
    #
    # except:
    #     print('No data present! Kinldy import your tasks first')
    #     return
    tasks = {'Version Control': 0, 'Agile Methodology': 0, 'Programming Logic': 0}
    tasknames = tasks.keys()

    if len(args) == 1 and args[0] == 'taskman.py' and args[1] == '-h':
        print('Usage: taskman.py taskname action\n\n'
              'Where taskname is the particular task.\n\n'
              '        Action is the command (status, or % complete)')
        return None
    elif len(args) == 2 and args[1] in action:
        actions(tasks, args)

    elif len(args) == 3 and args[1] in tasknames and args[2] in action:
        taskevaluator(tasks, args)


def taskevaluator(args):
    '''
    Function to evaluate the arguments an if valid execute!
    :param args:
    :return:
    '''
def actions(tasks, args):
    '''
    function to commit tasks
    :param argument:
    :return:
    '''
    if args[1] == 'jobs':
        print(tasks.keys())

    elif args[1] == 'status':
        print(statusEvaluator(tasks))
    elif args[2] == 'completed':
        completed(tasks, args[1])

def statusEvaluator(tasks):

    for value in tasks.values():
        i = 0
        if value == 1:
            i += 1
    print('{} Tasks out {} Completed!'.format(i, len(tasks.values())

def completed(tasks, arg):
        tasks[arg] = 1
        print(arg + 'Completed Successfully')
        pass



if __name__ == "__main__":
   main(sys.argv)