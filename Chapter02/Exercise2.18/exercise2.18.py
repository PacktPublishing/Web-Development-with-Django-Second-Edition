#!/usr/bin/env python3

from reviews.models import Publisher

publishers = Publisher.objects.filter(Q(name__startswith="New") | Q(name__endswith="Publisher"))

new_town_publisher = Publisher.objects.get(name='New Town Publisher')

publishers.contains(new_town_publisher)

publishers.contains(Publisher.objects.get(name='Byron Bay Press'))