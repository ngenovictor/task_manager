import sys




def main(args):
    '''

    :param sys:
    :return:
    '''

    try:
        with contextlib.closing(shelve.open(data, 'c')) as data:
            tasks = data['tasklist']
            time = data['time']

            tasknames = tasks.keys()

    except:
        print('No data present! Kinldy import your tasks first')
        return

    if

    if len(args) == 1 and args[0] == 'taskman.py' and args[1] == '-h':
        print('Usage: taskman.py taskname action\n\n'
              'Where taskname is the particular task.\n\n'
              '        Action is the command (status, or % complete)')
        return None
    elif len(args) == 2 and args[1] in tasknames :

        taskevaluator(args)

        print('Usage Error.\n\n'
              'Usage: CurrentWeatherrr.py city\n'
              'Where city is the town you would like to get the current weather conditions.')
        return 'Help'

def taskevaluator(args):






if __name__ == "__main__":
   main(sys.argv)