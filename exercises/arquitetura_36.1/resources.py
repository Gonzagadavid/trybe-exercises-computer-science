import subprocess

print('Processador:', subprocess.check_output('lscpu').decode('UTF-8'), '\n ------------------ \n')
print('RAM:', subprocess.check_output('free'), '\n ------------------ \n')
