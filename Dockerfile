FROM matrixdotorg/synapse:latest

# COPY synapse-swift-storage-provider /synapse-swift-storage-provider

RUN apk update && \
    apk add --no-cache \
      g++ \
      libffi-dev \
      git \
      python3-dev && \
    pip install --upgrade pip && \
    git clone https://github.com/iokiwi/synapse-swift-storage-provider.git && \
    cd /synapse-swift-storage-provider && \
    pip install . && \
    mkdir -p  /root/.config/openstack && \
    apk del \
        git \
        g++ \
        libffi-dev \
        python3-dev && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

# COPY clouds.yaml /root/.config/openstack/
