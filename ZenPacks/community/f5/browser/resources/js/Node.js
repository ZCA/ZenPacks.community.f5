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
ZC.registerName('BigipLtmNode', _t('Node'), _t('Nodes'));

/*
 * Custom component grid panel. This controls the grid that gets displayed for
 * components of the type set in "componentType".
 */
ZC.BigipLtmNodePanel = Ext.extend(ZC.ComponentGridPanel, {
	subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
        	autoExpandColumn: 'ltmNodeAddrAddr',
            componentType: 'BigipLtmNode',
            sortInfo: {
                field: 'ltmNodeAddrAddr',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                //{name: 'name'},
                {name: 'severity'},
                {name: 'ltmNodeAddrAddr'},
                {name: 'ltmNodeAddrScreenName'},
                {name: 'ltmNodeAddrRouteDomain'},
                {name: 'ltmNodeAddrStatusEnabledState'},
                {name: 'ltmNodeAddrStatusAvailState'},
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
            /*
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            */
            },{
                id: 'ltmNodeAddrAddr',
                dataIndex: 'ltmNodeAddrAddr',
                header: _t('IP Address'),
                width: 100
            },{
                id: 'ltmNodeAddrScreenName',
                dataIndex: 'ltmNodeAddrScreenName',
                header: _t('Screen Name'),
                width: 200
            },{
                id: 'ltmNodeAddrRouteDomain',
                dataIndex: 'ltmNodeAddrRouteDomain',
                header: _t('Route Domain'),
                width: 100
            },{
                id: 'ltmNodeAddrStatusEnabledState',
                dataIndex: 'ltmNodeAddrStatusEnabledState',
                header: _t('Enabled/Disabled'),
                sortable: true,
                width: 100
            },{
                id: 'ltmNodeAddrStatusAvailState',
                dataIndex: 'ltmNodeAddrStatusAvailState',
                header: _t('Availability Status'),
                sortable: true,
                width: 200
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.BigipLtmNodePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('BigipLtmNodePanel', ZC.BigipLtmNodePanel);


})();