pip3 install -r requirements.txt -t .\repos\resources\python

IF %1=="" (
    echo "it blank"
    rmdir /q /s cdk.out

    cdk synth
) ELSE (
    cdk synth --no-staging > template.yaml
)