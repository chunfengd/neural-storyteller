FROM somatic/k802x

#get this resolved
#https://github.com/ryankiros/neural-storyteller/blob/master/README.md
#A recent version of NumPy and SciPy <-- should already be in k802x
#Lasagne  nate you need to add this
#A version of Theano that Lasagne supports <-- and this

# Lasagne
RUN pip install -r https://raw.githubusercontent.com/Lasagne/Lasagne/master/requirements.txt
RUN pip install https://github.com/Lasagne/Lasagne/archive/master.zip


# RUN cd /home/ubuntu/somaticagent/ && git pull
RUN git clone https://github.com/chunfengd/neural-storyteller /home/ubuntu/experiment
# RUN cd /home/ubuntu/experiment && python setup.py install
# ADD .docker-experimentconfig /home/ubuntu/experiment/.experimentconfig

RUN cd /home/ubuntu/experiment/ && git pull
# RUN cd /home/ubuntu/somaticagent/ && git pull
# RUN cd /home/ubuntu/somaticagent/ && pip install -r requirements.txt
