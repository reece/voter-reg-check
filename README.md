# voter-reg-check

An experimental interface to check voter registration


## Development

    $ make devready
    $ source venv/3.8/bin/activate


## Running a local instance

Once installed as above, you should be able to:

    $ voter-reg-check-service seqrepo-rest-service

The navigate to the URL shown in the console output.


## Running a docker image

A docker image is available.  Invoke like this:

    $ docker run \
      --name voter-reg-check \
      --detach --rm -p 5000:5000 \
      reece/voter-reg-check
