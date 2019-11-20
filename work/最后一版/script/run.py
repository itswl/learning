from deploy import Deploy
import sys
import deploy_common



def main():
    cmd = sys.argv[1]
    if cmd == 'uninstall':
        deploy.logging.info('start uninstall ')
        deploy.uninstall()

    elif cmd == 'install':
        deploy.logging.info('start install')
        deploy.uninstall()
        deploy.unzip_package()
        deploy.init_plugin()
        deploy.cp_files()
        deploy.upload_deployparameter()
        deploy.deploy_start()
        deploy.configmgr_install_finish()

    elif cmd == 'retry':
        deploy.logging.info('start retry ')
        deploy.retry()

if __name__ == '__main__':
    with deploy_common.cost_time():
        deploy = Deploy()
        deploy.logging.info(deploy)
        main()
