import sai2

def main():    
    file_system = sai2.FileSystem()
    
    while True:
        command = input(f'{file_system.current_directory()}$ ')
    
        if command.startswith('mkdir '):
             _, directory_name = command.split(' ', 1)
             file_system.mkdir(directory_name)
        
        elif command.startswith('cd '):
            _, path = command.split(' ', 1)
            file_system.cd(path)
        
        elif command.startswith('ls'):
            if len(command.split()) > 1:
                _, path = command.split(' ', 1)
                file_system.ls(path)
            else:
                file_system.ls()
        
        elif command.startswith('touch '):
            _, file_names = command.split(' ', 1)
            file_names = file_names.split()
            for file_name in file_names:
                file_system.touch(file_name)
        
        elif command.startswith('echo '):
            _, rest = command.split(' ', 1)
            if '>>' in rest:
                text, file_path = rest.split('>>', 1)
                append=True
            else:
                text, file_path = rest.split('>', 1)
                append=False

            if text.startswith('-e '):
                text = text[3:-1]
                if (text.startswith('"') and text.endswith('"')) or (text.startswith("'") and text.endswith("'")):
                    lines = text[1:-1].split('\\n')
                else:
                    lines = [text]
            else:
                lines = [text]

            file_system.echo(lines, file_path.strip(), append)
        
        elif command.startswith('cat '):
            _, file_path = command.split(' ', 1)
            file_system.cat(file_path)
        
        elif command.startswith('rm'):
            _, file_path = command.split(' ', 1)
            file_system.rm(file_path)
        
        elif command == 'exit':
            break
        
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()