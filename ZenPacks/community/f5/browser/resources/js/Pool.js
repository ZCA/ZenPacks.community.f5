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
ZC.registerName('BigipLtmPool', _t('Pool'), _t('Pools'));

/*
 * Custom component grid panel. This controls the grid that gets displayed for
 * components of the type set in "componentType".
 */
ZC.BigipLtmPoolPanel = Ext.extend(ZC.ComponentGridPanel, {
	subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
        	autoExpandColumn: 'name',
            componentType: 'BigipLtmPool',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'ltmPoolActiveMemberCnt'},
                {name: 'ltmPoolMemberCnt'},
                {name: 'ltmPoolStatusEnabledState'},
                {name: 'ltmPoolStatusAvailState'},
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
                id: 'ltmPoolActiveMemberCnt',
                dataIndex: 'ltmPoolActiveMemberCnt',
                header: _t('Active Members'),
                sortable: true,
                width: 100
            },{
                id: 'ltmPoolMemberCnt',
                dataIndex: 'ltmPoolMemberCnt',
                header: _t('Total Members'),
                sortable: true,
                width: 100
            },{
                id: 'ltmPoolStatusEnabledState',
                dataIndex: 'ltmPoolStatusEnabledState',
                header: _t('Enabled/Disabled'),
                sortable: true,
                width: 100
            },{
                id: 'ltmPoolStatusAvailState',
                dataIndex: 'ltmPoolStatusAvailState',
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
        ZC.BigipLtmPoolPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('BigipLtmPoolPanel', ZC.BigipLtmPoolPanel);


})();