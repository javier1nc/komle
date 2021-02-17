import os
import sys
from suds.client import Client
from typing import Union

if 'komle.bindings.v1411.write' in sys.modules:
    # Witsml uses the same namespace for each schema
    # So for now check what binding is in use
    from komle.bindings.v1411.write import witsml
else:
    # Default to import read_bindings
    from komle.bindings.v1411.read import witsml

def simple_client(service_url: str, username: str, password: str, agent_name: str='komle') -> Client:
    '''Create a simple soap client using Suds, 
    
    This initializes the client with a local version of WMLS.WSDL 1.4 from energistics.

    Args:
        service_url (str): url giving the location of the Store
        username (str): username on the service
        password (str): password on the service
        agent_name (str): User-Agent name to pass in header 

    Returns:
        client (Client): A suds client with wsdl
    '''

    client = Client(f'file:{os.path.join(os.path.dirname(__file__), "WMLS.WSDL")}', 
                    username=username, 
                    password=password, 
                    location=service_url)

    client.set_options(headers={'User-Agent':agent_name})

    return client

class StoreClient:
    def __init__(self, service_url: str, username: str, password: str, agent_name: str='komle'):
        '''Create a GetFromStore client, 
        
        This initializes the client with a local version of WMLS.WSDL 1.4 from energistics.
    
        Args:
            service_url (str): url giving the location of the Store
            username (str): username on the service
            password (str): password on the service
            agent_name (str): User-Agent name to pass in header
        '''
    
        self.soap_client = simple_client(service_url,
                                         username,
                                         password,
                                         agent_name)
    
    def get_bhaRuns(self, 
                    q_bha: witsml.obj_bhaRun,
                    OptionsIn: str='returnElements=id-only') -> witsml.bhaRuns:
        '''Get bhaRuns from a witsml store server
    
        The default is only to return returnElements=id-only, change to all when you know what bhaRun to get.
    
    
        Args:
            q_bha (witsml.obj_bhaRun): A query bhaRun specifing objects to return, can be an empty bhaRun
            OptionsIn (str): String describing data to get on of [returnElements=all, returnElements=id-only, returnElements=header-only, 
                                                                       returnElements=data-only, returnElements=station-location-only,
                                                                       returnElements=latest-change-only, returnElements=requested,
                                                                       returnElements=data-only;requestLatestValues=500]
        Returns:
            witsml.bhaRuns: bhaRuns a collection of bhaRun
        
        Raises:
            pyxb.exception: If the reply is empty or the document fails to validate a pyxb exception is raised
        '''
    
        q_bhas = witsml.bhaRuns(version=witsml.__version__)
    
        q_bhas.append(q_bha)

        QueryIn = q_bhas.toxml()

        #OptionsIn=f'returnElements={returnElements}'
    
        reply_bhas = self.soap_client.service.WMLS_GetFromStore('bhaRun',
                                                                QueryIn,
                                                                OptionsIn
                                                               )
    
        return witsml.CreateFromDocument(reply_bhas.XMLout)


    def get_logs(self, 
                 q_log: witsml.obj_log,
                 OptionsIn: str='returnElements=id-only') -> witsml.logs:
        '''Get logs from a witsml store server
    
        The default is to return returnElements=id-only, change to all when you know what log to get.
        Pass an empty log with OptionsIn returnElements=id-only to get all by id.
    
    
        Args:
            q_log (witsml.obj_log): A query log specifing objects to return, for example uidWell, uidWellbore or an empty log
            OptionsIn (str): String describing data to get on of [returnElements=all, returnElements=id-only, returnElements=header-only, 
                                                                       returnElements=data-only, returnElements=station-location-only,
                                                                       returnElements=latest-change-only, returnElements=requested,
                                                                       returnElements=data-only;requestLatestValues=500]
        Returns:
            witsml.logs: logs a collection of log
        
        Raises:
            pyxb.exception: If the reply is empty or the document fails to validate a pyxb exception is raised
        '''
    
        q_logs = witsml.logs(version=witsml.__version__)
    
        q_logs.append(q_log)

        QueryIn = q_logs.toxml()


        #OptionsIn = f'returnElements={returnElements}'
    
        reply_logs = self.soap_client.service.WMLS_GetFromStore('log',
                                                                QueryIn,
                                                                OptionsIn
                                                               )

        return witsml.CreateFromDocument(reply_logs.XMLout)

    def get_mudLogs(self, 
                    q_mudlog: witsml.obj_mudLog,
                    OptionsIn: str='returnElements=id-only') -> witsml.mudLogs:
        '''Get mudLogs from a witsml store server
    
        The default is only to return id-only, change to all when you know what mudLog to get.
        Pass an empty mudLog with OptionsIn returnElements=id-only to get all by id.
    
    
        Args:
            q_mudlog (witsml.obj_mudLog): A query mudLog specifing objects to return, can be empty
            OptionsIn (str): String describing data to get on of [returnElements=all, returnElements=id-only, returnElements=header-only, 
                                                                       returnElements=data-only, returnElements=station-location-only,
                                                                       returnElements=latest-change-only, returnElements=requested,
                                                                       returnElements=data-only;requestLatestValues=500]
        Returns:
            witsml.mudLogs: mudLogs, a collection of mudLog
        
        Raises:
            pyxb.exception: If the reply is empty or the document fails to validate a pyxb exception is raised
        '''
    
        q_mudlogs = witsml.mudLogs(version=witsml.__version__)
    
        q_mudlogs.append(q_mudlog)

        QueryIn = q_mudlogs.toxml()

        #OptionsIn=f'returnElements={returnElements}'
    
        reply_mudlogs = self.soap_client.service.WMLS_GetFromStore('mudLog',
                                                                   QueryIn,
                                                                   OptionsIn
                                                                  )
    
        return witsml.CreateFromDocument(reply_mudlogs.XMLout)

    def get_trajectorys(self, 
                        q_traj: witsml.obj_trajectory,
                        OptionsIn: str='returnElements=id-only') -> witsml.trajectorys:
        '''Get trajectorys from a witsml store server
    
        The default is only to return returnElements=id-only, change to all when you know what trajectory to get.
        Pass an empty trajectory with OptionsIn returnElements=id-only to get all by id.
    
        Args:
            q_traj (witsml.obj_trajectory): A query trajectory specifing objects to return
            OptionsIn (str): String describing data to get on of [returnElements=all, returnElements=id-only, returnElements=header-only, 
                                                                       returnElements=data-only, returnElements=station-location-only,
                                                                       returnElements=latest-change-only, returnElements=requested,
                                                                       returnElements=data-only;requestLatestValues=500]
        Returns:
            witsml.trajectorys: trajectorys, a collection of trajectory
        
        Raises:
            pyxb.exception: If the reply is empty or the document fails to validate a pyxb exception is raised
        '''
    
        q_trajs = witsml.trajectorys(version=witsml.__version__)
    
        q_trajs.append(q_traj)

        QueryIn = q_trajs.toxml()

        #OptionsIn=f'returnElements={returnElements}
    
        reply_traj = self.soap_client.service.WMLS_GetFromStore('trajectory',
                                                                QueryIn,
                                                                OptionsIn
                                                               )
    
        return witsml.CreateFromDocument(reply_traj.XMLout)

    def get_wellbores(self, 
                      q_wellbore: witsml.obj_wellbore,
                      OptionsIn: str='returnElements=id-only') -> witsml.wellbores:
        '''Get wellbores from a witsml store server
    
        The default is only to return returnElements=id-only, change to all when you know what wellbore to get.
    
    
        Args:
            q_wellbore (witsml.obj_wellbore): A query wellbore specifing objects to return, can be an empty wellbore
            OptionsIn (str): String describing data to get on of [returnElements=all, returnElements=id-only, returnElements=header-only, 
                                                                       returnElements=data-only, returnElements=station-location-only,
                                                                       returnElements=latest-change-only, returnElements=requested,
                                                                       returnElements=data-only;requestLatestValues=500]
        Returns:
            witsml.wellbores: wellbores
        
        Raises:
            pyxb.exception: If the reply is empty or the document fails to validate a pyxb exception is raised
        '''
    
        q_wellbores = witsml.wellbores(version=witsml.__version__)
    
        q_wellbores.append(q_wellbore)

        QueryIn = q_wellbores.toxml()

        #OptionsIn=f'returnElements={returnElements}'
    
        reply_wellbores = self.soap_client.service.WMLS_GetFromStore('wellbore',
                                                                     QueryIn,
                                                                     OptionsIn
                                                                    )
    
        return witsml.CreateFromDocument(reply_wellbores.XMLout)