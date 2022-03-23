#!/usr/bin/env python3

from reviews.models import Publisher

Publisher.objects.bulk_create([
    Publisher(name="New Town Publisher", website="www.newtownexample.com", email='newtow@email.com'),
    Publisher(name="Byron Bay Press", website="www.byronbayexample.com", email='byronbayexample@email.com'),
    Publisher(name="Katoomba Publisher", website="www.katoombaexample.com", email='katoombaexample@email.com')]
)