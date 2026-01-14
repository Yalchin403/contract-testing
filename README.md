Run pact broker:

docker compose -f pact-broker.yml up -d


run consumer test to generate contract - pytest

pact-broker publish ms-tasks/tests/pacts \
  --consumer-app-version=1.0.0 \
  --broker-base-url=http://localhost:9292