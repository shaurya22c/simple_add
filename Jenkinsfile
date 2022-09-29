pipeline {
    agent any

    stages{

        stage('checkout'){
           steps{
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '55aec472-e876-415a-a546-d0ef907b7cc1', url: 'https://github.com/harsh-singhal7385/simple_add.git']]]) 
           }
        }
    
        stage('build'){
            steps{
                git branch: 'main', credentialsId: '55aec472-e876-415a-a546-d0ef907b7cc1', url: 'https://github.com/harsh-singhal7385/simple_add.git'
                sh 'python3 -m py_compile src/add2vals.py src/calc.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
        
        stage('test'){
            steps{
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }

            post{
                always{
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage('deliver'){
            steps{
                echo " great done with deploy / delivery of product..."
            }
        }

    }

}
