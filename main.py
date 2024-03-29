import filesystemclass

def main():    
    file_system = filesystemclass.FileSystem()    
    file_system.clear()
    while True:
        command = input(f'{file_system.current_directory()}$ ')
    
        if command.startswith('mkdir '):
             _, directory_name = command.split(' ', 1)
             file_system.mkdir(directory_name)
        
        elif command.startswith('cd '):
            _, path = command.split(' ', 1)
            file_system.cd(path)
        
        elif command.startswith('ls'):
            all_flag = False
            path=None
            if(len(command.split()) == 1):
                print(' '.join(file_system.ls(all_flag, path)))
            else:
                _, rest = command.split(' ', 1)
                if '-a' in rest.split():
                    all_flag = True
                    if len(rest.split()) > 1:
                        path = rest.split()[1]
                    print(' '.join(file_system.ls(all_flag, path)))
                else:
                    path = rest
                    print(' '.join(file_system.ls(all_flag, path)))                    
        
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
            print(file_system.cat(file_path))
        
        elif command.startswith('rm'):
            _, rest = command.split(' ', 1)
            if '-rf' in rest:
                _, path = rest.split(' ', 1)
                file_system.rm(path, True)
            else:
                file_system.rm(rest)
        
        elif command.startswith('mv '):
            _, source_path, destination_path = command.split(' ')
            file_system.mv(source_path, destination_path)
            
        elif command.startswith('cp '):
            if '-r' in command or '-R' in command:
                _, flag, source_path, destination_path = command.split(' ')
                file_system.cp(source_path, destination_path, True)
            else:
                _, source_path, destination_path = command.split(' ')
                file_system.cp(source_path, destination_path, False)
        
        elif command.startswith('grep '):
            rest, file_path = command.rsplit(maxsplit=1)
            start_quote_index = rest.find('"')
            end_quote_index = rest.rfind('"')
            if start_quote_index == -1 or end_quote_index == -1:
                print("Please put the pattern in double quotes")
                continue
            pattern = rest[start_quote_index + 1:end_quote_index]
            _,options = rest[:start_quote_index].split(' ', 1)
            options = options.split()        
            cnt = file_system.grep(file_path, pattern, not '-i' in options, '-w' in options, '-c' in options)
            if '-c' in options: print(cnt)

        elif command=='clear':
            file_system.clear()
        
        elif command == 'pwd':
            print(file_system.current_directory())
        
        elif command == 'exit':
            break
        
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()