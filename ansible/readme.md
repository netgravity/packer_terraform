# 



### create dir structure
mkdir -p roles/{base,baseEL8,monitoringServer}/{handlers,tasks,templates,files,vars,defaults,meta}

### Check
sunny@debby:generictools_vim$ tree
```.
└── roles
    ├── base
    │   ├── defaults
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── baseEL8
    │   ├── defaults
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    └── monitoringServer
        ├── defaults
        ├── files
        ├── handlers
        ├── meta
        ├── tasks
        ├── templates
        └── vars
```

In Ansible cfg turn hardware facts off to speed , since most of our env is vm
[defaults]
gather_subset=!hardware 

### Run Script
will run the roles per hosts , the var dir will have OS_family specific variables
ansible-playbook site.yml -K











### References
[Useful Vim Ansible blog](https://www.redhat.com/sysadmin/ansible-configure-vim)
