task :default => :test

desc "run tests"
task :test do
    sh "env py.test"
end

task :clean do
    sh "find . -name '__pycache__' | xargs rm -rf"
    sh "find . -name '*.pyc' | xargs rm -rf"
end
