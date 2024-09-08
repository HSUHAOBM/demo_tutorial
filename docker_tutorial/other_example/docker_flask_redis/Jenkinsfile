pipeline{
  agent any
//   {
//       label "agent"

//   }
  stages{
    stage("Delete Old Container"){
      steps {
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          echo "Delete the container"
        //   sh "docker rm -f run_mynode run_myweb"
        }
      }
    }
    stage("Building") {
      steps {
        echo "Building App"
        // sh docker-compose up -d
        // sh "cd ./app && docker build -t mynode:latest ."
        // sh "docker run -d -p 3000:3000 --name run_mynode --link my_postgres:my_postgres mynode:latest"

        // echo "Building FrontEnd"
        // sh "cd ./html && docker build -t myweb:latest ."
        // sh "docker run -d -p 8085:80 --name run_myweb --link run_mynode:run_mynode myweb:latest"
      }
    }

    stage("Test"){
      steps{
        echo "Testing begin testing2"
        sh "pwd"
      }
    }

    stage("Deploy"){
      steps{
        echo "deploy begin"
      }
    }
  }

  post {
    failure {
      echo "No!! it fail"
    }
    success {
      echo "Yes!! it work"
    }
  }
}