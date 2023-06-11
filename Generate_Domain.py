import random
import string
import datetime


def generate_domains(seed, count):
    random.seed(seed)
    tld = ['.com', '.net', '.org', '.info']
    domains = []
    for _ in range(count):
        domain_length = random.randint(8, 15)
        domain = ''.join(random.choice(string.ascii_lowercase)
                         for _ in range(domain_length))
        domain += random.choice(tld)
        domains.append(domain)
    return domains


def generate_seed():
    now = datetime.datetime.now()
    seed = now.strftime("%Y%m%d%H")
    return seed


domain_count = 10
seed = generate_seed()
domains = generate_domains(seed, domain_count)
for domain in domains:
    print(domain)
