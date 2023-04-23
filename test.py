import xml.etree.ElementTree as ET

def parse_kernel(kernel_xml):
    commands = []
    tree = ET.fromstring(kernel_xml)
    for child in tree:
        tag = child.tag.lower()
        if tag == 'script' or tag == 'envvar' or tag == 'envvars' or tag == 'input':
            continue
        if tag == 'cd':
            command = ['cd']
        else:
            command = [tag]
        args = []
        options = []
        for arg in child.findall('args'):
            args.append(arg.text.strip())
        for option in child.findall('option'):
            options.append(option.text.strip())
        command.extend(options)
        command.extend(args)
        commands.append(command)
    return commands

kernel_xml = '''<kernel>
                    <ls/>
                    <cd>
                        <args>
                            ~/Desktop
                        </args>
                    </cd>
                    <ls/>
                    <mkdir>
                        <args>
                            test
                        </args>
                    </mkdir>
                </kernel>'''

commands = parse_kernel(kernel_xml)
for i in range(len(commands)):
    commands[i] = " ".join(commands[i])

command = ";".join(commands)
print(command)
#Run command
import subprocess
subprocess.run(command, shell=True)