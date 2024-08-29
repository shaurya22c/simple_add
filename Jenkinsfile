pipeline {
    agent any

    stages{

        stage('checkout'){
           steps{
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '52bbabe0-a2a4-4c6d-ab43-e689f893ffb0', url: 'https://github.com/shaurya22c/simple_add.git']]]) 
           }
        }
    
        stage('build'){
            steps{
                git branch: 'main', credentialsId: '52bbabe0-a2a4-4c6d-ab43-e689f893ffb0', url: 'https://github.com/shaurya22c/simple_add.git'
                sh 'python3 -m py_compile src/add2vals.py src/calc.py'
                stash includes: 'src/*.py*', name: 'stashing_build'
            }
        }
        
        stage('test'){
            steps{
                sh 'python3 -m unittest src/test_calc.py'
            }
        }

        stage('deliver'){
            steps{
                echo " great done with deploy / delivery of product..."
            }
        }

    }

}
