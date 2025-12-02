## @ Sbl.py
#
#
# Copyright (c) 2018 - 2021, Intel Corporation. All rights reserved.<BR>
# Copyright (c) 2025 - 2026, Advantech Co Ltd. All rights reserved.<BR>
#
# SPDX-License-Identifier: BSD-2-Clause-Patent
#
##

import os
import sys
import re
import shutil
import argparse
import subprocess
from   datetime import date

##debug = "NO"
debug = "ALL"

def Fatal (msg):
    if debug == "ALL" :
        sys.stdout.flush()
        raise Exception (msg)

def Print (msg):
    if debug == "ALL" :
        print ('%s' % msg)

def GitCloneRepo (clone_dir, clone_repo, clone_commit):

    if clone_repo == '' and clone_commit == '':
        Fatal ('Failed to find repo and commit information!')

    Print (' clone_repo: %s\n clone_commit: %s' % (clone_repo, clone_commit))

    base_dir = os.path.basename(clone_dir)
    if base_dir == '$AUTO':
        repo_dir = os.path.basename(clone_repo)
        if repo_dir.lower().endswith('.git'):
            repo_dir = repo_dir[:-4]
        clone_dir = os.path.join (os.path.dirname(clone_dir), repo_dir)

    if not os.path.exists(clone_dir + '/.git'):
        Print ('Cloning the repo ... %s' % clone_repo)
        cmd = 'git clone %s %s' % (clone_repo, clone_dir)
        ret = subprocess.call(cmd.split(' '))
        if ret:
            Fatal ('Failed to clone repo to directory %s !' % clone_dir)
        Print ('GitCloneRepo - clone Done\n')

        if not clone_commit == '':
            Print ('Attempting to check out specified version ... %s' % clone_commit)
            cmd = 'git checkout %s' % clone_commit
            ret = subprocess.call(cmd.split(' '), cwd=clone_dir)
            if ret == 0:
                Print ('GitCloneRepo - checkout Done\n')
                return clone_dir
            else:
                Print ('GitCloneRepo - checkout: Failed to checkout  commit: %s' % clone_commit)
    else:
        # If the repository already exists, then try to check out the correct
        # revision without going to the network
        if not clone_commit == '':
            Print ('Attempting to check out specified version ... %s' % clone_commit)
            cmd = 'git checkout %s' % clone_commit
            ret = subprocess.call(cmd.split(' '), cwd=clone_dir)
            if ret == 0:
                Print ('GitCloneRepo - checkout Done\n')
                return clone_dir
            else:
                Print ('GitCloneRepo - checkout: Failed to checkout  commit: %s' % clone_commit)


def get_repo_git (arg_repo):
    platform_type ={
        'ahclsbl'    :   'https://github.com/mike04162003/AHCLSbl.git',
        'edk'        :   'https://github.com/mike04162003/EDK.git',
        'advgcipc'   :   'https://github.com/Advgcipc/slimbootloader.git',
        'sbl'        :   'https://github.com/slimbootloader/slimbootloader.git'
    }

    ModuleType = platform_type.get(arg_repo, "")

    return ModuleType

def get_advgcipc_commit (arg_platform):
    platform_type ={
        '688400S'    :   'SOM-6884',
        '6884A2S'    :   'SOM-6884A2',
        '758300S'    :   'SOM-7583',
        '599300S'    :   'SOM-5993',
        'D58000S'    :   'SOM-D580',
        'C35000S'    :   'SOM-C350',
        'DS20200'    :   'DS-202',
        'A28700A'    :   'AIMB-287',
        'A58600A'    :   'AIMB-586',
        '756900S'    :   'ADV'
    }

    ModuleType = platform_type.get(arg_platform, "")

    return ModuleType

def get_sbl_commit (arg_platform):
    platform_type ={
        '688400S'    :   '7a5041ee',
        '6884A2S'    :   '7a5041ee',
        '758300S'    :   '7a5041ee',
        '599300S'    :   '7a5041ee',
        'D58000S'    :   '7a5041ee',
        'C35000S'    :   '7a5041ee',
        'DS20200'    :   '7a5041ee',
        'A28700A'    :   '7a5041ee',
        'A58600A'    :   '7a5041ee',
        '756900S'    :   '7a5041ee'
    }

    ModuleType = platform_type.get(arg_platform, "")

    return ModuleType

def get_ahclsbl_commit (arg_platform):
    platform_type ={
        '688400S'    :   'SOM-6884',
        '6884A2S'    :   'SOM-6884A2',
        '758300S'    :   'SOM-7583',
        '599300S'    :   'SOM-5993',
        'D58000S'    :   'SOM-D580',
        'C35000S'    :   'SOM-C350',
        'DS20200'    :   'DS-202',
        'A28700A'    :   'AIMB-287',
        'A58600A'    :   'AIMB-586',
        '756900S'    :   'ADV'
    }

    ModuleType = platform_type.get(arg_platform, "")
    ModuleType = 'main'

    return ModuleType

def get_edk_commit (arg_platform):
    platform_type ={
        '688400S'    :   'SOM-6884',
        '6884A2S'    :   'SOM-6884A2',
        '758300S'    :   'SOM-7583',
        '599300S'    :   'SOM-5993',
        'D58000S'    :   'SOM-D580',
        'C35000S'    :   'SOM-C350',
        'DS20200'    :   'DS-202',
        'A28700A'    :   'AIMB-287',
        'A58600A'    :   'AIMB-586',
        '756900S'    :   'ADV'
    }

    ModuleType = platform_type.get(arg_platform, "")

    ModuleType = 'main'
    return ModuleType

def run_cmd(cmd_list):
    sys.stdout.flush()
    print (' '.join(cmd_list))
    ret = subprocess.call(cmd_list)
    if ret:
        sys.exit(1)

def Main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-g', dest='repo',    default = '', choices=['ahclsbl','edk','advgcipc','sbl'], help='specify git project name')
    ap.add_argument('-c', dest='commit',  default = '', choices=['main','688400S','6884A2S','758300S','599300S','D58000S','C35000S','DS20200','A28700A','A58600A','756900S'], help='specify commit id')
    args = ap.parse_args()

    repo_dir = os.path.abspath (os.path.join(os.getcwd(), '$AUTO'))
    repo = get_repo_git (args.repo)
    commit = ''

    if args.repo == 'advgcipc':
        commit = get_advgcipc_commit (args.commit)
    if args.repo == 'ahclsbl':
        commit = get_ahclsbl_commit (args.commit)
    if args.repo == 'edk':
        commit = get_edk_commit (args.commit)     
    if args.repo == 'sbl':
        commit = get_sbl_commit (args.commit)

    Print ("repo_dir :  %s\n"  % repo_dir)
    Print ("    repo :  %s\n"  % repo)
    Print ("  commit :  %s\n"  % commit)

    GitCloneRepo (repo_dir, repo, commit)
#    script_dir = os.path.abspath (os.path.join(os.getcwd(), 'AHCLSbl','Tools'))
#    Print ("script_dir :  %s\n"  % script_dir)
#    run_cmd([sys.executable, os.path.join(script_dir, 'AHCLSbl.py')])

 
    return 0

if __name__ == '__main__':
    sys.exit(Main())
