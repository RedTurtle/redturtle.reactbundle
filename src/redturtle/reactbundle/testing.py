# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing import z2

import redturtle.reactbundle


class RedturtleReactbundleLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=redturtle.reactbundle)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'redturtle.reactbundle:default')


REDTURTLE_REACTBUNDLE_FIXTURE = RedturtleReactbundleLayer()


REDTURTLE_REACTBUNDLE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(REDTURTLE_REACTBUNDLE_FIXTURE,),
    name='RedturtleReactbundleLayer:IntegrationTesting',
)


REDTURTLE_REACTBUNDLE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(REDTURTLE_REACTBUNDLE_FIXTURE,),
    name='RedturtleReactbundleLayer:FunctionalTesting',
)


REDTURTLE_REACTBUNDLE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        REDTURTLE_REACTBUNDLE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RedturtleReactbundleLayer:AcceptanceTesting',
)
