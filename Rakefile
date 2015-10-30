task :default => :test

namespace :db do
    desc "Create the database tables"
    task :create do
        sh "env python scripts/db/create.py"
    end

    desc "Destroy the database"
    task :destroy do
        sh "env python scripts/db/destroy.py"
    end

    desc "Recreate the database"
    task :do_over => [:destroy, :create]
end

desc "Run tests"
task :test do
    sh "env py.test"
end

desc "Clean temp and build files"
task :clean do
    sh "find . -name '__pycache__' | xargs rm -rf"
    sh "find . -name '*.pyc' | xargs rm -rf"
end
