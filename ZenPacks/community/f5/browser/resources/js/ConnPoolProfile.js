/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an ExampleDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');


/*
 * Friendly names for the components. First parameter is the meta_type in your
 * custom component class. Second parameter is the singular form of the
 * friendly name to be displayed in the UI. Third parameter is the plural form.
 */
ZC.registerName('BigipLtmConnPoolProfile', _t('OneConnect Profile'), _t('OneConnect Profiles'));

/*
 * Custom component grid panel. This controls the grid that gets displayed for
 * components of the type set in "componentType".
 */
ZC.BigipLtmConnPoolProfilePanel = Ext.extend(ZC.ComponentGridPanel, {
	subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
        	autoExpandColumn: 'name',
            componentType: 'BigipLtmConnPoolProfile',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'LtmConnPoolProfileMaxSize'},
                {name: 'LtmConnPoolProfileMaxAge'},
                {name: 'LtmConnPoolProfileMaxReuse'},
                {name: 'LtmConnPoolProfileIdleTimeout'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'LtmConnPoolProfileMaxSize',
                dataIndex: 'LtmConnPoolProfileMaxSize',
                header: _t('Max Size'),
                sortable: true,
                width: 100
            },{
                id: 'LtmConnPoolProfileMaxAge',
                dataIndex: 'LtmConnPoolProfileMaxAge',
                header: _t('Max Age'),
                sortable: true,
                width: 100
            },{
                id: 'LtmConnPoolProfileMaxReuse',
                dataIndex: 'LtmConnPoolProfileMaxReuse',
                header: _t('Max Reuse'),
                sortable: true,
                width: 100
            },{
                id: 'LtmConnPoolProfileIdleTimeout',
                dataIndex: 'LtmConnPoolProfileIdleTimeout',
                header: _t('Idle Timeout'),
                sortable: true,
                width: 100
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.BigipVirtualServerPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('BigipLtmConnPoolProfilePanel', ZC.BigipLtmConnPoolProfilePanel);


})();