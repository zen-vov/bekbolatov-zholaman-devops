import jenkins.model.Jenkins
import hudson.security.HudsonPrivateSecurityRealm
import hudson.security.FullControlOnceLoggedInAuthorizationStrategy
import org.jenkinsci.plugins.workflow.job.WorkflowJob
import org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition
import hudson.plugins.git.GitSCM

def j = Jenkins.get()
def realm = new HudsonPrivateSecurityRealm(false)
def password = new File('/run/secrets/jenkins_admin_password').text.trim()
realm.createAccount('zholaman', password)
j.setSecurityRealm(realm)
def auth = new FullControlOnceLoggedInAuthorizationStrategy()
auth.setAllowAnonymousRead(false)
j.setAuthorizationStrategy(auth)
j.setNumExecutors(1)
j.setSystemMessage('DevOps laboratory - Zholaman Bekbolatov / IT2-2314 / 37614')
def job = j.getItem('Bekbolatov_Zholaman_DevOps') ?: j.createProject(WorkflowJob, 'Bekbolatov_Zholaman_DevOps')
def scm = new GitSCM('https://github.com/zen-vov/bekbolatov-zholaman-devops.git')
scm.branches = [new hudson.plugins.git.BranchSpec('*/main')]
job.setDefinition(new CpsScmFlowDefinition(scm, 'Jenkinsfile'))
job.save()
j.save()
