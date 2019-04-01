import top_level_module

def print_one_script():
    print('Hello from', __name__)

if __name__ == '__main__':
    print_one_script()
    top_level_module.print_top_level_module()
