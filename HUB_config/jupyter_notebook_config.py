from nb2kg import managers

c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False

c.NotebookApp.session_manager_class=managers.SessionManager
c.NotebookApp.kernel_manager_class=managers.RemoteKernelManager
c.NotebookApp.kernel_spec_manager_class=managers.RemoteKernelSpecManager


# https://github.com/jupyter/notebook/issues/3130
c.FileContentsManager.delete_to_trash = False