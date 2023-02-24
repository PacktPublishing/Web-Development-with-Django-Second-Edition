#!/usr/bin/env python3

from reviews.models import Publisher

publishers = [Publisher.objects.get(name='New Town Publisher'), Publisher.objects.get(name='Byron Bay Press')]

publishers[0].website = "www.newsouthwalespublisher.com"
publishers[1].website = "www.newsouthwalespublisher.com"

Publisher.objects.bulk_update(publishers, ["website"])