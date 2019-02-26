from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
import os

def before_all(context):
    context.ansible_base_dir='/'.join(context.config.base_dir.split('/')[:-1])+'/ansible'

    loader = DataLoader()
    sources=context.ansible_base_dir+'/hosts'

    context.inventory = InventoryManager(loader=loader, sources=sources) if os.path.isfile(sources) else None
