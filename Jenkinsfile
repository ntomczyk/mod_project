node {
    stage('Cleanup') {
        step([$class: 'WsCleanup'])
    }
    stage('Checkout SCM') {
        checkout scm
    }
    def pythonImage
    stage('build docker image') {
        pythonImage = docker.build("maxsum:build")
    }
    stage('test') {
        pythonImage.inside {
            sh '. /tmp/venv/bin/activate && python -m pytest --junitxml=reports/xml_reports/report.xml --alluredir=reports/allure-reports'
        }
    }
    stage('collect test results') {
        junit 'reports/xml_reports/report.xml'
    }
}