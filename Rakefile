task :default => :test

VENV = "env"

def venv(command)
    sh "env #{command}"
end

namespace :build do
    desc "Initialize the environment"
    task :init do
        unless Dir.exists? VENV
            sh "virtualenv -p python2.7 #{VENV}"
        end
    end

    desc "Build the environment for production"
    task :prod => :init do
        venv "pip install -U -r requirements.txt"
    end

    desc "Build the environment for testing"
    task :test => :init do
        venv "pip install -U -r requirements.txt -r requirements-test.txt"
    end
end

namespace :db do
    desc "Create the database tables"
    task :create do
        venv "python scripts/db/create.py"
    end

    desc "Destroy the database"
    task :destroy do
        venv "python scripts/db/destroy.py"
    end

    desc "Recreate the database"
    task :do_over => [:destroy, :create]
end

desc "Run tests"
task :test do
    venv "py.test"
end

desc "Clean temp and build files"
task :clean do
    sh "find . -name '__pycache__' | xargs rm -rf"
    sh "find . -name '*.pyc' | xargs rm -rf"
end
