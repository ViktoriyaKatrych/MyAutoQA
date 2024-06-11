import pytest
from modules.api.clients.github import GitHub

#===== General tests. Test users ===========
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exist(github_api):
    user = github_api.get_user('ktrvktr')
    print(user)
    assert user['message']=='Not Found'

#test repositories
@pytest.mark.api
def test_repo_can_be_found(github_api):
    repos= github_api.search_repo('become-qa-auto')
    
    k=repos['total_count']
    print(f'Total Count:{k}')
    print({repos['items'] [0] ['name']})

    assert repos['total_count'] == 58
    assert 'become-qa-auto' in repos['items'] [0] ['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repos = github_api.search_repo('viktoriya_ktrch_no')
   
    k=repos['total_count']
    print(f'Total Count:{k}')
       
    assert repos['total_count'] ==0 


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    repos = github_api.search_repo('v')

    k=repos['total_count']
    print(f'Total Count:{k}')
    print({repos['items'] [0] ['name']})
   
    assert repos['total_count'] !=0  


#======= My Test Emojis. Individual task. ============

@pytest.mark.apiemo
def test_emo_exist(github_api):
    icon = github_api.get_emo('white_circle')

    assert icon != None
    
    print(f'Icon "white_circle" is on link: {icon}')
    
  
@pytest.mark.apiemo
def test_emo_no_exist(github_api):
    icon = github_api.get_emo('white_circlehhh')
      
    assert icon == None
        
    print('No icon "white_circlehhh"')    
    

#======= My Test commit. Individual task.============

@pytest.mark.apicommit
def test_commit_realdata(github_api):
    comm = github_api.get_commit('ViktoriyaKatrych', 'NewAutoQA', 'main')
    
    d = comm['commit']['author']
    print(d)
    assert d['name'] == 'Viktoriya Katrych'
    assert d['email'] == 'vkatrych@gmail.com'

    f = comm['commit']['message']
    print(f)
    print(comm['commit']['url'])


@pytest.mark.apicommit
def test_commit_otherREPO(github_api):
    comm = github_api.get_commit('ViktoriyaKatrych', 'WorkAutoQA', 'main')
    
    d = comm['commit']['author']
    print(d)
    assert d['name'] == 'ViktoriyaKatrych'
    assert d['email'] == 'vkatrych@gmail.com'
    
    f = comm['commit']['message']
    print(f)
    print(comm['commit']['url'])


@pytest.mark.apicommit
def test_commit_noexists_owner(github_api):
    comm = github_api.get_commit('ViktoriyaKatrych111', 'WorkAutoQA', 'main')
    print(comm)
   
    assert comm['message'] == 'Not Found'
    print('No Owner') 


@pytest.mark.apicommit
def test_commit_noexists_REPO(github_api):
    comm = github_api.get_commit('ViktoriyaKatrych', 'wwqeWorkAutoQA', 'main')
    print(comm)

    assert comm['message'] == 'Not Found'
    print('No REPO') 
      