# - from https://cloud.google.com/datalab/docs/quickstart

# VERIFY prereqs
gcloud components update
gcloud components install datalab

# CREATE Instance
datalab create datalab-lynntest

# CONNECT to Instance
http://localhost:8081


# ---------------REMOVE ALL---------------

# DELETE the VM
datalab delete datalab-lynntest
# DELTE the Persistent Disk
datalab delete --delete-disk datalab-lynntest
# DELETE the Firewall Rule
gcloud compute firewall-rules delete datalab-network-allow-ssh
# DELETE the Network
gcloud compute networks delete datalab-network
# DELETE the Repo
gcloud source repos delete datalab-notebooks

# ------------------TIPS:---------------------
# CREATE Instance with GPU -- fails (wrong region?)
datalab beta create-gpu datalab-lynntest-gpu

# CONNECTION (if terminal window is closed)
 datalab connect datalab-lynntest
 datalab connect --zone us-east1-b --port 8081 datalab-lynntest